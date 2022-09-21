from sql_alchemy import banco

class HotelModel(banco.Model):

    tablename = 'hoteis'
    id_hotel = banco.Column(banco.Integer, primary_key=True)
    nome_hotel = banco.Column(banco.String(80))
    estrelas_hotel = banco.Column(banco.Float(precision=1))
    diaria_hotel = banco.Column(banco.Float(precision=2))
    cidade_hotel = banco.Column(banco.String(40))



    def init(self, nome_hotel, estrelas_hotel, diaria_hotel, cidade_hotel):
        self.nome_hotel = nome_hotel
        self.estrelas_hotel = estrelas_hotel
        self.diaria_hotel = diaria_hotel
        self.cidade_hotel = cidade_hotel

    def json (self):
        return {
            'hotel': self.id_hotel,
            'nome': self.nome_hotel,
            'estrelas': self.estrelas_hotel,
            'diaria': self.diaria_hotel,
            'cidade': self.cidade_hotel
        }


    @classmethod
    def find_hotel(cls, id_hotel):
        hotel = cls.query.filter_by(id_hotel=id_hotel).first()# SELECT * FROM hotel WHERE id_hotel = $id_hotel
        if hotel:
            return hotel
        return None