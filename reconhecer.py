import cv2
import sqlite3


def reconhecerFace():

    classificador = cv2.CascadeClassifier(
        cv2.data.haarcascades +
        "haarcascade_frontalface_default.xml"
    )

    reconhecedor = cv2.face.LBPHFaceRecognizer_create()

    reconhecedor.read(
        "classificadorLBPH_V1.yml"
    )

    conexao = sqlite3.connect("banco.db")
    cursor = conexao.cursor()

    camera = cv2.VideoCapture(0)

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

            rosto = cv2.resize(
                imagemCinza[y:y+a, x:x+l],
                (200, 200)
            )

            id, confianca = reconhecedor.predict(
                rosto
            )

            if confianca < 80:

                cursor.execute(
                    "SELECT nome, cargo FROM pessoas WHERE id = ?",
                    (id,)
                )

                pessoa = cursor.fetchone()

                if pessoa:

                    nome = pessoa[0]
                    cargo = pessoa[1]

                else:

                    nome = "Nao encontrada"
                    cargo = ""
            else:
                nome = "Desconhecido"
                cargo = ''

            cv2.rectangle(
                imagem,
                (x, y),
                (x+l, y+a),
                (0, 255, 0),
                2
            )

            identComp = f'{nome} - {cargo}'
            cv2.putText(
                imagem,
                identComp,
                (x, y-10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.5,
                (0, 255, 0),
                2
            )

        cv2.imshow("Reconhecimento", imagem)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    camera.release()
    conexao.close()
    cv2.destroyAllWindows()