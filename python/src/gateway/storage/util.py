import pika
import json
import logging

logging.basicConfig(level=logging.INFO)


def upload(f, fs, channel, access):
    try:
        fid = fs.put(f)
    except Exception as err:
        logging.error(f"Failed to upload file: {err}")
        return "Internal Server Error", 500

    message = {
        "video_fid": str(fid),
        "mp3_fid": None,
        "username": access["username"],
    }

    try:
        channel.basic_publish(
            exchange="",
            routing_key="video",
            body=json.dumps(message),
            properties=pika.BasicProperties(
                delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE
            ),
        )
    except Exception as err:
        fs.delete(fid)
        logging.error(f"Failed to publish message to RabbitMQ: {err}")
        return "Internal Server Error", 500
