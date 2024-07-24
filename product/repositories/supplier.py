from typing import List, Optional

from product.models import Supplier,Category, Product


class SupplierRepository:
    def get_all(self) -> List[Supplier]:
        return Supplier.objects.all()
    
    def get_by_id(self, id: int)-> Supplier:
        return Supplier.objects.get(id=id)
    
    def filter_by_id(self, id: int)-> Optional[Supplier]:
        return Supplier.objects.filter(id=id).first()
    
    def delete(self, supplier: Supplier):
        return supplier.delete()

    def update(
            self,
            supplier: Supplier,
            name: str,
            address: str,
            phone: str,
    ):
            supplier.name = name
            supplier.address = address
            supplier.phone = phone
            supplier.save()

    def create(
            self,
            name: str,
            address: str,
            phone: str,
    )->Supplier:
        return Supplier.objects.create(
            name=name,
            address=address,
            phone=phone,
        )