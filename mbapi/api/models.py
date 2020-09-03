# -*- coding: utf-8 -*-
"""
@author: Rosario Distefano
@email: rosario.distefano@osumc.edu
"""

from enum import Enum
from fastapi import Query
from pydantic import BaseModel, Field
from pydantic.validators import dict_validator
from typing import Any, Dict, List, Optional, Union


class OrganismKind(BaseModel):
    """Used to manage supported organisms"""
    organism: str = Field(..., example="human")

class OrganismKindRNAmod(OrganismKind):
    """Used to manage supported organisms"""
    mod_type: str = Field(..., example="ai")

class OrganismKindRNAmodChrStemloopMirna(OrganismKindRNAmod):
    """Used to manage supported biological sources"""
    chromosome: Optional[str] = None
    stemloop: Optional[str] = None
    mirna: Optional[str] = None

class StudiesInfo(BaseModel):
    """Used to manage studies info"""
    organism: str
    mod_type: str
    pubmed_id: int
    author: str
    year: int

class SearchBy(OrganismKind):
    """Used to manage supported search"""
    mod_type: str
    chromosome: Optional[str] = None
    start: Optional[int] = None
    end: Optional[int] = None
    strand: Optional[str] = None
    stemloop: Optional[str] = None
    mirna: Optional[str] = None
    biological_source: Optional[str] = None
    class Config:
        schema_extra = {
            "example": {
                "organism": "human",
                "mod_type": "ai",
                "chromosome": "1",
                "start": 1167160,
                "end": 1167166,
                "strand": "+"
            }
        }

class SearchByRNAES(OrganismKind):
    """Used to manage supported search"""
    mod_type: str
    chromosome: str
    strand: str
    genomic_position: int
    biological_source: Optional[str] = None
    class Config:
        schema_extra = {
            "example": {
                "organism": "human",
                "mod_type": "ai",
                "chromosome": "1",
                "strand": "+",
                "genomic_position": 1167164
            }
        }

class RNAESStudy(BaseModel):
    """Used to manage RNA Editing site studies basic info"""
    pubmed_id: int
    author: str
    year: int
    reported_effects: str
    details: str
    impaired_targeting: str
    target_gaining: str
    enzyme_selectivity: str 
    validation_methods_and_functional_characterization: Dict[str, str]
    site_specific_detection_methods: Dict[str, str]
    verification_methods: Dict[str, str]
    physiological_pathological_condition: List[Dict[str,Any]]

class RNAfold(BaseModel):
    """Used to manage RNAfold prediction basic info"""
    wildtype_rna_2d_structure: Optional[str] = None
    wildtype_free_energy: Optional[float] = None
    wildtype_mea: Optional[float] = None
    wildtype_seq: Optional[str] = None
    edited_rna_2d_structure: Optional[str] = None
    edited_free_energy: Optional[float] = None
    edited_mea: Optional[float] = None
    edited_seq: Optional[str] = None

class UriInfo(BaseModel):
    """Used to manage external resources info"""
    darned: Optional[str] = None
    rediportal: Optional[str] = None
    radar: Optional[str] = None
    ucsc: Optional[str] = None

class RNAESBasicInfo(BaseModel):
    """Used to manage RNA Editing site basic info"""
    organism: str
    mod_type: str
    chromosome: str
    strand: str
    genomic_position: int
    transcript_region: str
    stemloop: str
    stemloop_acc_number: str
    stemloop_region_involved: str
    stemloop_local_pos: Optional[int] = None
    mirna: Optional[str] = None
    mirna_acc_number: Optional[str] = None
    mirna_local_pos: Optional[int] = None
    motif_5_to_3: Optional[str] = None
    rnafold_stemloop: RNAfold
    uri: UriInfo
    prediction: bool
    enrichment: bool

class RNAESFullInfo(RNAESBasicInfo):
    """Used to manage RNA Editing site full info"""
    stemloop_local_pos: Optional[int] = None
    mirna: Optional[str] = None
    mirna_local_pos: Optional[int] = None
    mirna_seq: Optional[str] = None
    studies: List[RNAESStudy]

class PredictionVennInfo(BaseModel):
    """Used to manage RNAfold prediction basic info"""
    refseq: str
    gene_name: Optional[str] = None

class PredictionBasicInfo(PredictionVennInfo):
    """Used to manage RNAfold prediction basic info"""
    ensembl_id: Optional[str] = None
    gene_biotype: Optional[str] = None
    miranda: int
    rnahybrid: int
    targetscan: int
    pita: int
    mirmap: int
    consensus: int

class PredictionInfo(BaseModel):
    """Used to manage GO Terms.
    """
    wildtype: List[PredictionBasicInfo] = []
    edited: List[PredictionBasicInfo] = []
    wildtype_unique: List[PredictionVennInfo] = []
    edited_unique: List[PredictionVennInfo] = []
    intersection: List[PredictionVennInfo] = []

class RNAESPredictionInfo(BaseModel):
    """Used to manage RNA Editing site basic info"""
    organism: str
    mod_type: str
    chromosome: str
    strand: str
    genomic_position: int
    stemloop: str
    stemloop_acc_number: str
    stemloop_local_pos: int
    mirna: str
    mirna_acc_number: str
    mirna_local_pos: int
    mirna_seq: str
    target_prediction: PredictionInfo

class GoTermVennInfo(BaseModel):
    """Used to manage GO Term venn info"""
    go_id : str
    go_name: str

class GoTermInfo(BaseModel):
    """Used to manage GO Term basic info"""
    go_id : str
    adj_pvalue: float
    go_name: str
    targets_list: List[str] = []
    go_namespace: str
    pvalue: float

class EnrichmentGoInfo(BaseModel):
    """Used to manage GO Terms"""
    wildtype: List[GoTermInfo] = []
    edited: List[GoTermInfo] = []
    wildtype_unique: List[GoTermVennInfo] = []
    edited_unique: List[GoTermVennInfo] = []
    intersection: List[GoTermVennInfo] = []

class GoTermCategoryInfo(BaseModel):
    """Used to manage GO Term categories"""
    mf: EnrichmentGoInfo
    bp: EnrichmentGoInfo
    cc: EnrichmentGoInfo

class PathwayVennInfo(BaseModel):
    """Used to manage Pathway venn info"""
    pathway_id : str
    pathway_name: str

class PathwayInfo(BaseModel):
    """Used to manage Pathway basic info"""
    pathway_id : str
    adj_pvalue: float
    pathway_name: str
    targets_list: List[str] = []
    pvalue: float

class EnrichmentPathwayInfo(BaseModel):
    """Used to manage Pathways"""
    wildtype: List[PathwayInfo] = []
    edited: List[PathwayInfo] = []
    wildtype_unique: List[PathwayVennInfo] = []
    edited_unique: List[PathwayVennInfo] = []
    intersection: List[PathwayVennInfo] = []

class EnrichmentInfo(BaseModel):
    """Used to manage enrichment data"""
    go: GoTermCategoryInfo
    kegg: EnrichmentPathwayInfo
    reactome: EnrichmentPathwayInfo

class RNAESEnrichmentInfo(BaseModel):
    """Used to manage RNA Editing site enrichment basic info"""
    organism: str
    mod_type: str
    chromosome: str
    strand: str
    genomic_position: int
    stemloop: str
    stemloop_acc_number: str
    stemloop_local_pos: int
    mirna: str
    mirna_acc_number: str
    mirna_local_pos: int
    target_enrichment: EnrichmentInfo

class BiologicalSourceInfo(BaseModel):
    """Used to manage GO Terms"""
    organism: str
    mod_type: str
    biological_source: str

class CompareBy(OrganismKind):
    """Used to manage supported comparison"""
    mod_type: str
    stemloop: Optional[str] = None
    disease: Optional[str] = None
    class Config:
        schema_extra = {
            "example": {
                "organism": "human",
                "mod_type": "ai",
                "disease": "blood (hematopoietic stem cells)"
            }
        }

class CompareInfo(BaseModel):
    """Used to manage comparison editing levels"""
    compared_with: Optional[str] = None
    avg_perc_editing_in_normal: Optional[float] = None
    avg_perc_editing_in_adverse: Optional[float] = None
    editing_levels_in_individual_sample: Optional[str] = None

class EditingLevel(BaseModel):
    """Used to manage editing levels"""
    el_from: Optional[str] = None 
    el_to: Optional[str] = None

class ExperimentType(BaseModel):
    """Used to manage experiment types"""
    in_vitro: Optional[str] = None 
    ex_vivo: Optional[str] = None 
    in_vivo: Optional[str] = None 

class RNAELevel(BaseModel):
    """Used to manage the RNA Editing level"""
    primirna: EditingLevel
    premirna: EditingLevel
    mirna: EditingLevel

class ComparisonBasicInfo(BaseModel):
    """Used to manage comparison basic info"""
    biological_source: Optional[str] = None
    editing: RNAELevel
    experiment_type: ExperimentType
    pathological_vs_physiological_comparison: CompareInfo

class ComparisonInfo(BaseModel):
    """Used to manage comparison info"""
    organism: str
    mod_type: str
    chromosome: str
    strand: str
    genomic_position: int
    transcript_region: str
    stemloop: str
    stemloop_acc_number: Optional[str] = None
    stemloop_region_involved: Optional[str] = None
    stemloop_local_pos: Optional[int] = None
    mirna: Optional[str] = None
    mirna_seq: Optional[str] = None
    mirna_acc_number: Optional[str] = None
    mirna_local_pos: Optional[int] = None
    author: str
    year: int
    pubmed_id: int
    physiological_pathological_condition: ComparisonBasicInfo

