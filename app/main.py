from fastapi import FastAPI
from app.analyzer import analyze_resources
from app.ai_engine import generate_ai_report

app = FastAPI()

@app.get("/")
def home():
    return {
        "message": "AI Cloud Cost Detective Running"
    }

@app.get("/findings")
def findings():

    data = analyze_resources()

    return {
        "findings": data
    }

@app.get("/report")
def report():

    findings = analyze_resources()

    ai_report = generate_ai_report(findings)

    return {
        "report": ai_report
    }

@app.get("/savings")
def savings():

    findings = analyze_resources()

    total = sum(item["monthly_cost"] for item in findings)

    return {
        "estimated_monthly_savings": total,
        "estimated_yearly_savings": total * 12
    }
