from dataclasses import dataclass
@dataclass
class Product:
    id: int
    name: str
    category: str
    price: float
    stock: int
    created_at: str