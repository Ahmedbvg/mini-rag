from pydantic import BaseModel 
from typing import Optional

class processRequest(BaseModel):
    file_id: str=None
    chunk_size: Optional[int] = 100 # Default chunk size is 100 bytes
    overlap_size: Optional[int] = 20 # Default overlap size is 20 bytes
    do_reset: Optional[int] = 0
