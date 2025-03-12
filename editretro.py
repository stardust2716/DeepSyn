from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/run-script")
def run_script():
    try:
        # 执行Shell脚本
        result = subprocess.run(['sh', 'your_script.sh'], capture_output=True, text=True, check=True)
        return {"message": "脚本执行成功", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"message": "脚本执行失败", "error": e.stderr}