from typing import List,Optional, NoReturn

from product.models import Category

class CategoryRepository:
    def get_all(self) -> List[Category]:
        return  Category.objects.all()
    
    def get_by_id(self, id: int)-> Category:
        return Category.objects.get(id=id)

    def filter_by_id(self, id: int) -> Optional[Category]:
        return Category.objects.filter(id=id).first()
    
    def delete(self, category: Category):
        category.delete()

    def update(
            self,
            category: Category,
            nombre: str,
    ):
            category.name = nombre
            category.save()
    
    def create(
        self,
        nombre: str,
    )->Category:
        return Category.objects.create(
            name=nombre,
        )