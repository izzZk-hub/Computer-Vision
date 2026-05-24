from deepface import DeepFace
import cv2

video = cv2.VideoCapture(0)

print("Sistema iniciado...")

while True:
    ret, frame = video.read()

    nombre = "No reconocido"

    try:
        result = DeepFace.find(
            img_path=frame,
            db_path="faces",
            enforce_detection=False
        )

        if len(result[0]) > 0:
            nombre = result[0]["identity"][0].split("/")[-1]
            print("Reconocido:", nombre)

    except:
        nombre = "No reconocido"

    # mostrar texto en pantalla
    cv2.putText(frame, nombre, (50, 50),
                cv2.FONT_HERSHEY_SIMPLEX, 1,
                (0, 0, 255) if nombre == "No reconocido" else (0, 255, 0),
                2)

    cv2.imshow("Sistema de Reconocimiento", frame)

    # salir con q
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()