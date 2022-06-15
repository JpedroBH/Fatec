from datetime import datetime
from django.test import TestCase
from .models import FeriadoModel
from .utils.FeriadosAPI import FeriadoAPI

class Feriado_Test(TestCase):

    def setUp(self):
        self.feriado = 'Natal'
        self.data = datetime.strptime('2022-12-25','%Y-%m-%d').date()

        self.FeriadoCad = FeriadoModel(nome=self.feriado, data=self.data)
        self.FeriadoCad.save()

    def test_feriado_novo(self):
        self.assertTrue(FeriadoModel.objects.exists())

    def test_nome(self):
        self.assertEqual(self.FeriadoCad.nome, self.feriado)

    def test_data(self):
        self.assertEqual(self.FeriadoCad.data, self.data)




class Feriado_Test(TestCase):

    def test_objeto(self):

        objeto = FeriadoAPI(2022)
        assert objeto._ano, 2022
        assert type(objeto.feriados) == list
        assert len(objeto.feriados) == 11


    def test_str(self):

        objeto = FeriadoAPI(2023)
        msg = 'Feriados de 2023'
        assert str(objeto) == msg
        assert repr(objeto) == msg


    def test_str(self):

        objeto = FeriadoAPI(2022)
        msg = 'Feriados de 2022'
        assert str(objeto) == msg
        assert repr(objeto) == msg


    def test_propriedades(self):

        objeto = FeriadoAPI(2022)
        assert objeto.ano == '2022'
