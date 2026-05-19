import cv2
import os
import numpy as np
from PIL import Image


def treinarModelo():

    faces = []
    ids = []

    caminhoFotos = "fotos"

    for pessoa in os.listdir(caminhoFotos):

        pastaPessoa = os.path.join(
            caminhoFotos,
            pessoa
        )

        for foto in os.listdir(pastaPessoa):

            caminhoFoto = os.path.join(
                pastaPessoa,
                foto
            )

            imagem = Image.open(
                caminhoFoto
            ).convert('L')

            imagemNP = np.array(
                imagem,
                'uint8'
            )

            faces.append(imagemNP)

            ids.append(int(pessoa))

    reconhecedor = cv2.face.LBPHFaceRecognizer_create()

    reconhecedor.train(
        faces,
        np.array(ids)
    )

    reconhecedor.save(
        "classificadorLBPH_V1.yml"
    )

    print("Modelo treinado!")