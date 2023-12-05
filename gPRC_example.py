import grpc
import audio2face_pb2
import audio2face_pb2_grpc

#Install Requiremnts

# pip install grpcio grpcio-tools
# & also
# python -m grpc_tools.protoc -I /path/to/protos --python_out=. --grpc_python_out=. audio2face.proto


def send_audio_to_audio2face(audio_data):
    # Create a gRPC channel to the Audio2Face server
    channel = grpc.insecure_channel('localhost:50051')  # Replace with actual server address and port

    # Create a stub (client) for the Audio2Face service
    stub = audio2face_pb2_grpc.Audio2FaceStub(channel)

    # Create an audio data message
    audio_message = audio2face_pb2.AudioDataRequest(audio_data=audio_data)

    # Make a gRPC request to the streaming audio player server
    response = stub.StreamAudio(audio_message)

    # Process the response if needed
    print("Response:", response.message)

# Example: Replace this with your actual audio loading logic
audio_data = b'\x00\x01\x02...'  # Replace with actual audio data

# Send audio to Audio2Face
send_audio_to_audio2face(audio_data)

# Ensure that the Audio2Face gRPC server is running and accessible at the specified address and port.