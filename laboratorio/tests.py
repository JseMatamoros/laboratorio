from django.test import TestCase, Client
from django.urls import reverse
from .models import Laboratorio

class LaboratorioViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.index_url = reverse('index')
        self.mostrar_url = reverse('mostrar_laboratorios')
        self.insertar_url = reverse('insertar_laboratorio')
        self.editar_url = reverse('editar_laboratorio', args=[1])
        self.eliminar_url = reverse('eliminar_laboratorio', args=[1])
    
    def test_index_view(self):
        response = self.client.get(self.index_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
    
    def test_mostrar_laboratorios_view(self):
        response = self.client.get(self.mostrar_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'mostrar_laboratorios.html')
    
    def test_insertar_laboratorio_view(self):
        response = self.client.get(self.insertar_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'insertar_laboratorio.html')
    
    def test_editar_laboratorio_view(self):
        # Crear un objeto de laboratorio para utilizar su id en la URL de edición
        laboratorio = Laboratorio.objects.create(nombre='Laboratorio 1', ciudad='Ciudad 1', pais='País 1')
        editar_url = reverse('editar_laboratorio', args=[laboratorio.id])
        response = self.client.get(editar_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'editar_laboratorio.html')
    
    def test_eliminar_laboratorio_view(self):
        # Crear un objeto de laboratorio para utilizar su id en la URL de eliminación
        laboratorio = Laboratorio.objects.create(nombre='Laboratorio 1', ciudad='Ciudad 1', pais='País 1')
        eliminar_url = reverse('eliminar_laboratorio', args=[laboratorio.id])
        response = self.client.get(eliminar_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'eliminar_laboratorio.html')
