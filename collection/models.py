from django.db import models

# Create your models here.

class Image(models.Model):
    name = models.CharField(max_length = 60)
    pic = models.ImageField(upload_to = 'uploads')
    description = models.TextField()
    image_location = models.ForeignKey('Location')
    image_category = models.ForeignKey('Category')



    @classmethod
    def get_all_images(cls):
        images = cls.objects.all()
        return images



    def delete_image(self):
        self.delete()


    @classmethod
    def get_image_by_id(cls,image_id):
        image = cls.objects.filter(image_id= id).all()
        return image

    @classmethod
    def get_image_by_cat(cls,category):
        images = cls.objects.filter(image_category__category_name__icontains=category).all()
        return images

    @classmethod
    def get_image_by_location(cls,location):
        images = cls.objects.filter(image_location__location_name__icontains=location).all()
        return images

    def __str__(self):
        return self.name


class Location(models.Model):
    locations = (
        ('Nairobi','Nairobi'),
        ('Zurich','Zurich'),
        ('Paris','Paris'),
        ('Munich','Munich'),
        ('Tokyo','Tokyo'),
        ('London','London'),
        ('Melbourne','Melbourne'),
        ('Sydney','Sydney'),
        ('Berlin','Berlin')
    )

    loc = models.CharField(max_length=255, choices=locations)

    class Meta:
        verbose_name_plural = 'Location'

    def __str__(self):
        return f"{self.loc}"




    def save_location(self):
        self.save()



class Category(models.Model):
    categories = (
        ('Food','Food'),
        ('Cars','Cars'),
        ('Shoes','Shoes'),
        ('Quotes','Quotes')
    )

    cat = models.CharField(max_length = 255, choices = categories)


    class Meta:
        verbose_name_plural = 'Category'


    def __str__(self):
        return f"{self.cat}"




    def save_category(self):
        self.save()


    def delete_category(self):
        self.delete()