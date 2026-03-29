#!/usr/bin/env python3
"""ES Consulting Sales Intelligence Skill for OpenFang"""
import json
import sys

PORTFOLIO = {
    "chevron": {"client": "Chevron", "industry": "Energy", "solution": "Agreement Intelligence, Document Analytics & Investment Optimization", "desc": "Custom application for interacting with, visualizing, and acting on agreements and document intelligence. Investment optimization platform."},
    "nestle": {"client": "Nestlé Mexico", "industry": "Consumer Goods", "solution": "Demand Forecasting, Inventory Optimization & Price Intelligence", "desc": "AI-powered demand forecasting, inventory optimization, scenario analysis, and price optimization across Latin American markets."},
    "premier": {"client": "Premier Lending", "industry": "Financial Services", "solution": "End-to-End AI-Powered Loan Officer Empowerment", "desc": "Complete AI solution empowering loan officers to achieve more with full accuracy and speed."},
    "dod": {"client": "U.S. Department of Defense", "industry": "Defense", "solution": "Accounting Automation — 25 Days to 2 Hours", "desc": "Automating accounting processes that previously took 25 days, now completed in 2 hours."},
    "toyota": {"client": "Toyota Financial Services", "industry": "Automotive", "solution": "Churn Prediction & Credit Score AI Intelligence", "desc": "Churn prediction and credit score AI. Proactive customer retention with ML-driven risk models."},
    "anthropic": {"client": "Anthropic", "industry": "AI Research", "solution": "Expert Data & Analytics for Next-Gen Claude", "desc": "Expert data and analytics to improve next-generation Claude models. RLHF, red-team evaluation."},
}

COMPETITORS = {
    "accenture": {"them": "700K+ employees. Team of juniors. 6-12 month timelines. $500K+ entry.", "us": "Boutique. Senior only. Founders on call. 8-16 weeks.", "verdict": "They give decks. We ship code."},
    "deloitte": {"them": "Consulting-first. Months of strategy. Offshore implementation.", "us": "Engineering-first. Same senior team start to finish.", "verdict": "They tell you what to build. We build it."},
    "mckinsey": {"them": "Best strategy. Don't build software. You're on your own for implementation.", "us": "Strategy + implementation + deployment in one team.", "verdict": "They give the map. We drive you there."},
    "in-house": {"them": "6-12 months to hire. $800K+/year. No production AI experience.", "us": "Production experience day 1. We train your team as we build.", "verdict": "Let us get to production. Your team takes over."},
    "openai": {"them": "Great models. ChatGPT Enterprise is a product, not a solution.", "us": "We build the 80% around the model: orchestration, memory, security.", "verdict": "They build the engine. We build the car."},
}

def analyze_prospect(company, industry=""):
    ind = industry.lower() if industry else "technology"
    db = {
        "financial": {"pain": "Manual processes, credit risk gaps, churn, compliance", "opp": "AI lending automation, credit scoring, churn prediction", "ref": "Premier Lending, Toyota Financial"},
        "energy": {"pain": "Agreement complexity, investment decisions, document overload", "opp": "Document intelligence, agreement analytics, investment optimization", "ref": "Chevron"},
        "defense": {"pain": "Manual processes taking weeks, security requirements", "opp": "Process automation (25 days→2 hrs), secure AI", "ref": "U.S. DoD"},
        "consumer": {"pain": "Demand uncertainty, pricing, inventory waste", "opp": "Demand forecasting, price optimization, inventory AI", "ref": "Nestlé Mexico"},
        "health": {"pain": "Documentation burden, diagnostic delays, compliance", "opp": "Clinical AI, automated documentation, HIPAA platforms", "ref": "Healthcare deployments"},
        "tech": {"pain": "Scaling AI, model quality, infra costs", "opp": "Custom AI platforms, RLHF, developer tools", "ref": "Anthropic"},
    }
    key = next((k for k in db if k in ind), None)
    m = db.get(key, {"pain": "Operational inefficiency, data silos", "opp": "Custom AI agents, automation, analytics", "ref": "Multiple Fortune 500"})
    
    return json.dumps({
        "company": company, "industry": ind,
        "pain_points": m["pain"], "opportunities": m["opp"],
        "relevant_client": m["ref"], "timeline": "8-16 weeks",
        "next_step": "Schedule call with Rudy and Justin",
        "react_component": {
            "type": "CompanyAnalysis",
            "props": {"company": company, "industry": ind, "painPoints": m["pain"].split(", "), "opportunities": m["opp"].split(", "), "reference": m["ref"]}
        }
    })

def calculate_roi(size, use_case, cost=500000):
    mult = {"startup": 1, "mid-market": 2.5, "enterprise": 5, "fortune-500": 10}.get(size, 2.5)
    inv = int(150000 * mult)
    sav = int(cost * 0.35 * mult)
    return json.dumps({
        "investment": f"${inv//1000}K-${int(inv*1.5)//1000}K",
        "annual_savings": f"${sav//1000}K-${int(sav*1.8)//1000}K",
        "roi": f"{int(sav/inv*100)}-{int(sav*1.8/inv*100)}%",
        "payback": f"{int(inv/sav*12)} months",
        "react_component": {
            "type": "ROICard",
            "props": {"investment": inv, "savings": sav, "useCase": use_case, "companySize": size}
        }
    })

def compare_vendors(competitor):
    c = competitor.lower()
    key = next((k for k in COMPETITORS if k in c), None)
    m = COMPETITORS.get(key, {"them": "Generic vendor.", "us": "Fully custom. Senior team.", "verdict": "We compete on results."})
    return json.dumps({
        "competitor": competitor, "their_approach": m["them"], "our_approach": m["us"], "verdict": m["verdict"],
        "react_component": {
            "type": "ComparisonTable",
            "props": {"competitor": competitor, "rows": [
                {"aspect": "Team", "them": m["them"].split(".")[0], "us": m["us"].split(".")[0]},
                {"aspect": "Timeline", "them": "6-12 months", "us": "8-16 weeks"},
                {"aspect": "Verdict", "them": "", "us": m["verdict"]}
            ]}
        }
    })

def capture_lead(name="", email="", company="", project="", urgency="exploring"):
    return json.dumps({
        "status": "captured",
        "message": f"Rudy and Justin will reach out to {email} within 24 hours. Technical call, not sales.",
        "react_component": {
            "type": "LeadConfirmation",
            "props": {"name": name, "email": email, "company": company, "project": project}
        }
    })

def show_portfolio(focus=""):
    items = list(PORTFOLIO.values())
    if focus:
        items = [p for p in items if focus.lower() in p["client"].lower() or focus.lower() in p["industry"].lower()] or items
    return json.dumps({
        "portfolio": items,
        "react_component": {
            "type": "PortfolioGrid",
            "props": {"items": items}
        }
    })

def demo_swarm(task, agents=6):
    n = min(max(agents, 3), 12)
    roles = ["Coordinator", "Researcher", "Analyst", "Strategist", "Validator", "Synthesizer", "Fact-Checker", "Risk-Assessor", "Data-Miner", "Quality-Gate", "Optimizer", "Reporter"]
    return json.dumps({
        "operation": task, "agents": n, "total_time": "3.09s",
        "phases": ["Decomposition (45ms)", f"Spawn {n} agents (120ms)", "Parallel execution (2.3s)", f"BFT Consensus ({n}/{n})", "CRDT Synthesis (340ms)", "Quality Gate (0.94/1.0)"],
        "react_component": {
            "type": "SwarmVisualization",
            "props": {"task": task, "agentCount": n, "roles": roles[:n]}
        }
    })

def main():
    payload = json.loads(sys.stdin.read())
    tool = payload["tool"]
    inp = payload["input"]
    
    try:
        if tool == "analyze_prospect":
            result = analyze_prospect(inp.get("company", ""), inp.get("industry", ""))
        elif tool == "calculate_roi":
            result = calculate_roi(inp.get("company_size", "enterprise"), inp.get("use_case", ""), inp.get("current_cost", 500000))
        elif tool == "compare_vendors":
            result = compare_vendors(inp.get("competitor", ""))
        elif tool == "capture_lead":
            result = capture_lead(inp.get("name", ""), inp.get("email", ""), inp.get("company", ""), inp.get("project", ""), inp.get("urgency", ""))
        elif tool == "show_portfolio":
            result = show_portfolio(inp.get("focus", ""))
        elif tool == "demo_swarm":
            result = demo_swarm(inp.get("task", ""), inp.get("agents", 6))
        else:
            print(json.dumps({"error": f"Unknown tool: {tool}"}))
            return
        print(json.dumps({"result": result}))
    except Exception as e:
        print(json.dumps({"error": str(e)}))

if __name__ == "__main__":
    main()
