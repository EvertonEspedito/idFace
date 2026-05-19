import cv2
import os
import time


def capturarFaces():

    idPessoa = input("Matricula da pessoa: ")

    pasta = f"fotos/{idPessoa}"

    os.makedirs(pasta, exist_ok=True)

    classificador = cv2.CascadeClassifier(
        cv2.data.haarcascades +
        "haarcascade_frontalface_default.xml"
    )

    camera = cv2.VideoCapture(0)

    contador = 0

    print("Captura iniciando...")
    print("Mova o rosto lentamente.")
    print("Pressione Q para sair.")

    while True:

        conectado, imagem = camera.read()

        if not conectado:
            break

        imagemCinza = cv2.cvtColor(
            imagem,
            cv2.COLOR_BGR2GRAY
        )

        faces = classificador.detectMultiScale(
            imagemCinza,
            scaleFactor=1.1,
            minNeighbors=5
        )

        for (x, y, l, a) in faces:

            rosto = imagemCinza[
                y:y+a,
                x:x+l
            ]

            rosto = cv2.resize(
                rosto,
                (200, 200)
            )

            contador += 1

            cv2.imwrite(
                f"{pasta}/{contador}.jpg",
                rosto
            )

            cv2.rectangle(
                imagem,
                (x, y),
                (x+l, y+a),
                (0, 255, 0),
                2
            )

            cv2.putText(
                imagem,
                f"Foto {contador}",
                (x, y - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 255, 0),
                2
            )

            # Espera 1.5 segundos
            time.sleep(1.5)

        cv2.imshow("Captura", imagem)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        if contador >= 5:
            break

    camera.release()
    cv2.destroyAllWindows()

    print("Faces capturadas!")