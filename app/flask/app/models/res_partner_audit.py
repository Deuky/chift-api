from typing import Optional
from sqlmodel import Field, SQLModel, Column, JSON

class ResPartnerAudit(SQLModel, table=True):
    __tablename__ = "res_partner_audit"
    id: Optional[int] = Field(default=None, primary_key=True)
    partner_id: int
    action: str
    data: dict = Field(default_factory=dict, sa_column=Column(JSON))

    class Config:
        arbitrary_types_allowed = True 
