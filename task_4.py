
import platform

def get_cpu_model():
    try:
        cpu_model = platform.processor()
        return cpu_model
    except Exception as e:
        print(f"Error retriving in CPU Model {e}")
        return None


cpu_model=get_cpu_model()
if cpu_model:
    print(f"CPU model :{cpu_model}")
else:
    print("Unabel to retrive CPU model")
    