from bson.objectid import ObjectId
from config.config import DB, CONF
from fastapi import APIRouter, Depends, HTTPException
from typing import List, Any, Optional
import logging

from .models import (
    OrganismKind,
    OrganismKindRNAmod,
    OrganismKindRNAmodChrStemloopMirna,
    SearchBy,
    SearchByRNAES,
    RNAfold,
    RNAESBasicInfo,
    RNAESFullInfo,
    RNAESPredictionInfo,
    RNAESEnrichmentInfo,
    CompareBy,
    ComparisonInfo,
    StudiesInfo
)

mb_router = APIRouter()

def validate_chromosome_range(start: Optional[int] = None, end: Optional[int] = None):
    if isinstance(start, int) and isinstance(end, int):
        if start < 0 or end < 0 or start > end:
            if CONF["fastapi"].get("debug", False):
                logging.warning(
                    "Invalid chromosome range. The `start` and `end` values "\
                    "must be positive integers, with start <= end."
                )
            raise HTTPException(
                status_code=400,
                detail="Invalid chromosome range. The `start` and `end` values "\
                    "must be positive integers, with start <= end."
            )
        return { "$gte": start, "$lte": end }
    elif isinstance(start, int):
        if start < 0:
            if CONF["fastapi"].get("debug", False):
                logging.warning(
                    "Invalid chromosome start. The `start` value must be "\
                    "a positive integer."
                )
            raise HTTPException(
                status_code=400, 
                detail="The `start` value must be a positive integer."
            )
        return { "$gte": start }
    elif isinstance(end, int):
        if end < 0:
            if CONF["fastapi"].get("debug", False):
                logging.warning(
                    "Invalid chromosome end. The `end` value must be "\
                    "a positive integer."
                )
            raise HTTPException(
                status_code=400, 
                detail="The `end` value must be a positive integer."
            )
        return { "$lte": end }
    else:
        return {}

def validate_object_id(id_: str):
    try:
        _id = ObjectId(id_)
    except Exception:
        if CONF["fastapi"].get("debug", False):
            logging.warning("Invalid Object ID")
        raise HTTPException(status_code=400)
    return _id

async def _get_pet_or_404(id_: str):
    _id = validate_object_id(id_)
    pet = await DB.editing_sites.find().limit(1)
    if pet:
        return pet
    else:
        raise HTTPException(status_code=404, detail="Pet not found")

@mb_router.get("/")
async def get_welcome():
    """Welcome
    """
    return {"description": "Welcome!"}

@mb_router.post(
    "/organisms/rnaenditingtypes/",
    response_model=List[str],
    summary="Get the organism's RNA Editing types list"
)
async def get_editing_types(item: OrganismKind):
    """
    Endpoint to retrieve the organisms's RNA Editing types.
    """
    cursor = await DB.editing_sites.distinct(
        "mod_type", 
        {"organism": item.organism}
    )
    return list(map(str, cursor))

@mb_router.post(
    "/organisms/chromosomes/",
    response_model=List[str],
    summary="Get the organism's chromosomes list"
)
async def get_chromosomes(item: OrganismKindRNAmod):
    """
    Endpoint to retrieve the organisms's chromosomes.
    """
    cursor = await DB.editing_sites.distinct(
        "chromosome", 
        {
            "organism": item.organism,
            "mod_type": item.mod_type
        }
    )
    return sorted(
        [v for v in list(map(str, cursor)) if v.isdigit()], 
        key=lambda x: int(x)
    ) + sorted([v for v in list(map(str, cursor)) if not v.isdigit()])

@mb_router.post(
    "/organisms/mirnas/",
    response_model=List[str],
    summary="Get the organism's miRNAs list"
)
async def get_mirnas(item: OrganismKindRNAmod):
    """
    Endpoint to retrieve the organisms's miRNAs.
    """
    cursor = await DB.editing_sites.distinct(
        "mirna", 
        {
            "organism": item.organism,
            "mod_type": item.mod_type,
            "mirna": { "$exists": True, "$ne": None }
        }
    )
    return list(map(str, cursor))

@mb_router.post(
    "/organisms/premirnas/",
    response_model=List[str],
    summary="Get the organism's pre-miRNAs (stem-loop) list"
)
async def get_premirnas(item: OrganismKindRNAmod):
    """
    Endpoint to retrieve the organisms's pre-miRNAs.
    """
    cursor = await DB.editing_sites.distinct(
        "stemloop", 
        {
            "organism": item.organism,
            "mod_type": item.mod_type,
            "stemloop": { "$exists": True, "$ne": None }
        }
    )
    return list(map(str, cursor))

@mb_router.post(
    "/organisms/biologicalsources/",
    response_model=List[str],
    summary="Get the organism's biological sources list"
)
async def get_biological_sources(item: OrganismKindRNAmodChrStemloopMirna):
    """
    Endpoint to retrieve the organisms's biological sources.
    """
    query = {
        "organism": item.organism,
        "mod_type": item.mod_type,
        "biological_source": { "$exists": True, "$ne": None }
    }

    if item.chromosome:
        query["chromosome"] = item.chromosome
    if item.stemloop:
       query["stemloop"] = item.stemloop
    if item.mirna:
       query["mirna"] = item.mirna

    cursor = await DB.biological_sources.distinct(
        "biological_source", 
        query
    )
    return list(map(str, cursor))

@mb_router.post(
    "/studies/",
    response_model=List[StudiesInfo],
    summary="Get the database studies list"
)
async def get_studies(item: OrganismKind):
    """Endpoint to retrieve the database studies list."""

    pipe = [
        {
            '$match': {
                'organism': item.organism
            }
        },
        {
            '$unwind': '$studies'
        },
        {
            '$group': {
                '_id': {
                    'pubmed_id': '$studies.pubmed_id',
                    'mod_type': '$mod_type'
                },
                'organism': { '$first': '$organism' },
                'mod_type': { '$first': '$mod_type' },
                'pubmed_id': { '$first': '$studies.pubmed_id' },
                'author': { '$first': '$studies.author' },
                'year': { '$first': '$studies.year' }
            }
        },
        {
            '$project': {
                'organism': 1,
                'mod_type': 1,
                'pubmed_id': 1,
                'author': 1,
                'year': 1,
                '_id': 0
            }
        }
    ]
    
    cursor = DB.editing_sites.aggregate(pipeline=pipe, allowDiskUse=True)
    results = []
    async for document in cursor:
        results.append(document)
    return results
    
    
@mb_router.post(
    "/organisms/rnaeditingsites/detail/",
    response_model=RNAESFullInfo,
    summary="Get the organism's RNA Editing site details"
)
async def get_editing_site_detail(item: SearchByRNAES):
    """
    Endpoint to retrieve the organisms's RNA Editing site details, according to
    a specific modification type (e.g., A-to-I), chromosome, strand, and genomic
    position.
    """
    query = {
        "organism": item.organism,
        "mod_type": item.mod_type,
        "chromosome": item.chromosome,
        "strand": item.strand,
        "genomic_position": item.genomic_position
    }

    if item.biological_source:
        query["studies.physiological_pathological_condition.biological_source"] = { "$in": item.biological_source.split(';') }
        pipe = [
            {
                "$unwind": "$studies"
            },
            {
                "$match": query,
            },
            {
                "$group": {
                    "_id": {
                        "pubmed_id": "$studies.pubmed_id"
                    },
                    "organism": { "$first": "$organism" },
                    "mod_type": { "$first": "$mod_type" },
                    "chromosome": { "$first": "$chromosome" },
                    "strand": { "$first": "$strand" },
                    "genomic_position": { "$first": "$genomic_position" },
                    "transcript_region": { "$first": "$transcript_region" },
                    "stemloop": { "$first": "$stemloop" },
                    "stemloop_region_involved": { "$first": "$stemloop_region_involved" },
                    "stemloop_local_pos": { "$first": "$stemloop_local_pos" },
                    "stemloop_acc_number": { "$first": "$stemloop_acc_number" },
                    "mirna": { "$first": "$mirna" },
                    "mirna_acc_number": { "$first": "$mirna_acc_number" },
                    "mirna_local_pos": { "$first": "$mirna_local_pos" },
                    "rnafold_stemloop": { "$first": "$rnafold_stemloop" },
                    "number_high_throughput_studies": { "$first": "$number_high_throughput_studies" },
                    "number_enzyme_perturbation_studies": { "$first": "$number_enzyme_perturbation_studies" },
                    "number_targeted_method_studies": { "$first": "$number_targeted_method_studies" },
                    "is_putative": { "$first": "$is_putative" },
                    "studies": { 
                        "$push":  "$studies"
                    },
                    "uri": { "$first": "$uri" },
                    "prediction": { "$first": "$prediction" },
                    "enrichment": { "$first": "$enrichment" }
                }
            },
            {
                "$project": {
                    "organism": 1,
                    "mod_type": 1,
                    "chromosome": 1,
                    "strand": 1,
                    "genomic_position": 1,
                    "transcript_region": 1,
                    "stemloop": 1,
                    "stemloop_region_involved": 1,
                    "stemloop_local_pos": 1,
                    "stemloop_acc_number": 1,
                    "mirna": 1,
                    "mirna_acc_number": 1,
                    "mirna_local_pos": 1,
                    "rnafold_stemloop": 1,
                    "number_high_throughput_studies": 1,
                    "number_enzyme_perturbation_studies": 1,
                    "number_targeted_method_studies": 1,
                    "is_putative": 1,
                    "studies": 1,
                    "uri": 1,
                    "prediction": 1,
                    "enrichment": 1,
                    "_id": 0
                }
            },
            {
                "$unwind": "$studies"
            },
            {
                "$group": {
                    "_id": {
                        "organism": "$organism",
                        "mod_type": "$mod_type",
                        "chromosome": "$chromosome",
                        "strand": "$strand",
                        "genomic_position": "$genomic_position"
                    },
                    "organism": { "$first": "$organism" },
                    "mod_type": { "$first": "$mod_type" },
                    "chromosome": { "$first": "$chromosome" },
                    "strand": { "$first": "$strand" },
                    "genomic_position": { "$first": "$genomic_position" },
                    "transcript_region": { "$first": "$transcript_region" },
                    "stemloop": { "$first": "$stemloop" },
                    "stemloop_region_involved": { "$first": "$stemloop_region_involved" },
                    "stemloop_local_pos": { "$first": "$stemloop_local_pos" },
                    "stemloop_acc_number": { "$first": "$stemloop_acc_number" },
                    "mirna": { "$first": "$mirna" },
                    "mirna_acc_number": { "$first": "$mirna_acc_number" },
                    "mirna_local_pos": { "$first": "$mirna_local_pos" },
                    "rnafold_stemloop": { "$first": "$rnafold_stemloop" },
                    "number_high_throughput_studies": { "$first": "$number_high_throughput_studies" },
                    "number_enzyme_perturbation_studies": { "$first": "$number_enzyme_perturbation_studies" },
                    "number_targeted_method_studies": { "$first": "$number_targeted_method_studies" },
                    "is_putative": { "$first": "$is_putative" },
                    "studies": { 
                        "$push":  "$studies"
                    },
                    "uri": { "$first": "$uri" },
                    "prediction": { "$first": "$prediction" },
                    "enrichment": { "$first": "$enrichment" }
                }
            },
            {
                "$project": {
                    "organism": 1,
                    "mod_type": 1,
                    "chromosome": 1,
                    "strand": 1,
                    "genomic_position": 1,
                    "transcript_region": 1,
                    "stemloop": 1,
                    "stemloop_region_involved": 1,
                    "stemloop_local_pos": 1,
                    "stemloop_acc_number": 1,
                    "mirna": 1,
                    "mirna_acc_number": 1,
                    "mirna_local_pos": 1,
                    "rnafold_stemloop": 1,
                    "number_high_throughput_studies": 1,
                    "number_enzyme_perturbation_studies": 1,
                    "number_targeted_method_studies": 1,
                    "is_putative": 1,
                    "studies": 1,
                    "uri": 1,
                    "prediction": 1,
                    "enrichment": 1,
                    "_id": 0
                }
            }
        ]

        cursor = DB.editing_sites.aggregate(pipeline=pipe, allowDiskUse=True)
        results = await cursor.to_list(length=1)
        return results[0] if results else {}
    else:
        return await DB.editing_sites.find_one(
            query, 
            {
                "organism": 1,
                "mod_type": 1,
                "chromosome": 1, 
                "strand": 1, 
                "genomic_position": 1,
                "transcript_region": 1,
                "stemloop": 1,
                "stemloop_acc_number": 1,
                "stemloop_region_involved": 1,
                "stemloop_local_pos" : 61,
                "mirna" : 1,
                "mirna_acc_number": 1,
                "mirna_local_pos": 1,
                "mirna_seq": 1,
                "motif_5_to_3": 1,
                "rnafold_stemloop": 1,
                "number_high_throughput_studies": 1,
                "number_enzyme_perturbation_studies": 1,
                "number_targeted_method_studies": 1,
                "is_putative": 1,
                "studies": 1,
                "uri": 1,
                "prediction": 1,
                "enrichment": 1,
                "_id": 0
            }
        )
    

@mb_router.post(
    "/organisms/rnaeditingsites/predictions/",
    response_model=RNAESPredictionInfo,
    summary="Get the organism's RNA Editing site target predictions"
)
async def get_editing_site_target_predictions(item: SearchByRNAES):
    """
    Endpoint to retrieve the organisms's RNA Editing site target predictions, according to
    a specific modification type (e.g., A-to-I), chromosome, strand, and genomic
    position.
    """
    query = {
        "organism": item.organism,
        "mod_type": item.mod_type,
        "chromosome": item.chromosome,
        "strand": item.strand,
        "genomic_position": item.genomic_position
    }

    cursor = DB.targets_prediction.find_one(
        query, 
        {
            "organism": 1,
            "mod_type": 1,
            "chromosome": 1, 
            "strand": 1, 
            "genomic_position": 1,
            "stemloop": 1,
            "stemloop_acc_number": 1,
            "stemloop_local_pos" : 61,
            "mirna" : 1,
            "mirna_acc_number": 1,
            "mirna_local_pos": 1,
            "mirna_seq": 1,
            "target_prediction": 1,
            "_id": 0
        }
    )

    return await cursor

@mb_router.post(
    "/organisms/rnaeditingsites/enrichment/",
    response_model=RNAESEnrichmentInfo,
    summary="Get the organism's RNA Editing site target enrichment"
)
async def get_editing_site_target_enrichment(item: SearchByRNAES):
    """
    Endpoint to retrieve the organisms's RNA Editing site target enrichment, according to
    a specific modification type (e.g., A-to-I), chromosome, strand, and genomic
    position.
    """
    query = {
        "organism": item.organism,
        "mod_type": item.mod_type,
        "chromosome": item.chromosome,
        "strand": item.strand,
        "genomic_position": item.genomic_position
    }

    cursor = DB.targets_enrichment.find_one(
        query, 
        {
            "organism": 1,
            "mod_type": 1,
            "chromosome": 1, 
            "strand": 1, 
            "genomic_position": 1,
            "stemloop": 1,
            "stemloop_acc_number": 1,
            "stemloop_local_pos" : 61,
            "mirna" : 1,
            "mirna_acc_number": 1,
            "mirna_local_pos": 1,
            "mirna_seq": 1,
            "target_enrichment": 1,
            "_id": 0
        }
    )

    return await cursor

@mb_router.post(
    "/organisms/rnaeditingsites/",
    response_model=List[RNAESBasicInfo],
    summary="Get the organism's RNA Editing sites list"
)
async def get_editing_sites(item: SearchBy):
    """
    Endpoint to retrieve the organisms's RNA Editing sites, according to
    a specific modification type (e.g., A-to-I). Optionally, it is possible
    to restrict results to a particular Chromosome, miRNA, or pre-miRNA.
    """
    chrom_range = validate_chromosome_range(item.start, item.end)

    query = {
        "organism": item.organism,
        "mod_type": item.mod_type
    }
    if item.chromosome:
        query["chromosome"] = item.chromosome
        if chrom_range:
            query["genomic_position"] = chrom_range
        if item.strand:
            query["strand"] = item.strand
        
    if item.stemloop:
       query["stemloop"] = item.stemloop
    if item.mirna:
       query["mirna"] = item.mirna

    if item.biological_source:
        query["studies.physiological_pathological_condition.biological_source"] = { "$in": item.biological_source.split(';') }

    cursor = DB.editing_sites.find(
        query, 
        {
            "organism": 1,
            "mod_type": 1,
            "chromosome": 1, 
            "strand": 1, 
            "genomic_position": 1,
            "transcript_region": 1,
            "stemloop": 1,
            "stemloop_region_involved": 1,
            "stemloop_local_pos": 1,
            "stemloop_acc_number": 1, 
            "mirna": 1,
            "mirna_acc_number": 1,
            "mirna_local_pos": 1,
            "rnafold_stemloop": 1,
            "uri": 1,
            "prediction": 1,
            "enrichment": 1,
            "number_high_throughput_studies": 1,
            "number_enzyme_perturbation_studies": 1,
            "number_targeted_method_studies": 1,
            "is_putative": 1,
            "_id": 0
        }
    )

    results = []
    async for document in cursor:
        results.append(document)
    return results

@mb_router.get(
    "/organisms/",
    response_model=List[str],
    summary="Get the organisms list"
)
async def get_organisms():
    """
    Endpoint to retrieve organisms.
    """
    cursor = await DB.editing_sites.distinct("organism")
    return list(map(str, cursor))


mbc_router = APIRouter()

@mbc_router.get(
    "/comparison/organisms/",
    response_model=List[str],
    summary="Get a list of available organisms"
)
async def get_comparison_organisms():
    """
    Endpoint to retrieve organisms.
    """
    cursor = await DB.case_vs_control_comparison.distinct("organism")
    return list(map(str, cursor))

@mb_router.post(
    "/comparison/rnaenditingtypes/",
    response_model=List[str],
    summary="Get a list of RNA modification types available for a specific organism"
)
async def get_comparison_rna_modification_types(item: OrganismKind):
    """
    Endpoint to retrieve the organisms's RNA modification types.
    """
    cursor = await DB.case_vs_control_comparison.distinct(
        "mod_type", 
        {"organism": item.organism}
    )
    return list(map(str, cursor))

@mbc_router.post(
    "/comparison/premirnas/",
    response_model=List[str],
    summary="Get the list of stem-loops available for a specific organism and RNA modification type"
)
async def get_comparison_premirnas(item: OrganismKindRNAmod):
    """
    Endpoint to retrieve a list of stem-loops (pre-miRNAs) for a specific
    organism and RNA modification type for the comparison analysis.
    """
    cursor = await DB.case_vs_control_comparison.distinct(
        "stemloop", 
        {
            "organism": item.organism,
            "mod_type": item.mod_type,
            "stemloop": { "$exists": True, "$ne": None }
        }
    )
    return sorted(list(map(str, cursor)))

@mbc_router.post(
    "/comparison/diseases/",
    response_model=List[str],
    summary="Get the list of diseases available for a specific organism and RNA modification type"
)
async def get_comparison_diseases(item: OrganismKindRNAmod):
    """
    Endpoint to retrieve list of diseases available for a specific organism
    and RNA modification type.
    """
    cursor = await DB.case_vs_control_comparison.distinct(
        "physiological_pathological_condition.biological_source", 
        {
            "organism": item.organism,
            "mod_type": item.mod_type,
            "physiological_pathological_condition.biological_source": { "$exists": True, "$ne": None }
        }
    )
    return sorted(list(map(str, cursor)))

@mbc_router.post(
    "/organisms/comparison/",
    response_model=List[ComparisonInfo],
    summary="Get the organism's case versus control comparisons list"
)
async def get_editing_site_comparison(item: CompareBy):
    """
    Endpoint to retrieve the organisms's case versus control comparisons , according to
    a specific modification type (e.g., A-to-I), biological source/pre-miRNA.
    """
    query = {
        "organism": item.organism,
        "mod_type": item.mod_type
    }
        
    if item.stemloop:
       query["stemloop"] = item.stemloop
    if item.disease:
       query["physiological_pathological_condition.biological_source"] = item.disease

    cursor = DB.case_vs_control_comparison.find(
        query, 
        {
            "organism": 1,
            "mod_type": 1,
            "chromosome": 1,
            "strand": 1,
            "genomic_position": 1,
            "author": 1, 
            "year": 1, 
            "pubmed_id": 1,
            "transcript_region": 1,
            "stemloop": 1,
            "stemloop_acc_number": 1,
            "stemloop_region_involved": 1,
            "stemloop_local_pos" : 1,
            "mirna" : 1,
            "mirna_seq": 1,
            "mirna_acc_number": 1,
            "mirna_local_pos": 1,
            "physiological_pathological_condition": 1,
            "_id": 0
        }
    )

    results = []
    async for document in cursor:
        results.append(document)

    return results