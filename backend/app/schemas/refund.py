from pydantic import BaseModel


class RefundRequest(BaseModel):
    order_id: str
    reason: str


class RefundApprovalRequest(BaseModel):
    thread_id: str
    approved: bool