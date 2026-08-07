ANALYTICS_HUB_SYSTEMS = {
"ihris": {
        "name": "Health Workforce",
        "badge": "HRH",
        "description": (
            "Health workforce analytics covering staffing levels, cadres, facilities, "
            "workforce distribution, and HRH reporting."
        ),
        "products": [
            {
                "id": "workforce-overview",
                "title": "Workforce Overview Dashboard",
                "type": "Dashboard",
                "status": "Prototype",
                "description": (
                    "Overview of health workforce distribution, staffing levels, "
                    "cadres, and facility-level HRH reporting."
                ),
                "url": "/superset/dashboard/8/?standalone=1",
            },
            {
                "id": "facility-staffing",
                "title": "Facility Staffing Dashboard",
                "type": "Dashboard",
                "status": "Coming soon",
                "description": (
                    "Facility staffing gaps, filled posts, vacant posts, and "
                    "staffing distribution."
                ),
                "url": None,
            },
            {
                "id": "cadre-distribution",
                "title": "Cadre Distribution Report",
                "type": "Report",
                "status": "Coming soon",
                "description": (
                    "Workforce distribution by cadre, district, facility, and "
                    "employment category."
                ),
                "url": None,
            },
            {
                "id": "hrh-data-quality",
                "title": "HRH Data Quality Checks",
                "type": "Data quality",
                "status": "Coming soon",
                "description": (
                    "Checks for missing staff records, duplicate personnel, "
                    "incomplete facility assignment, and inconsistent cadre values."
                ),
                "url": None,
            },
        ],
    },

    "elmis": {
        "name": "Supply Chain",
        "badge": "eLMIS",
        "description": (
            "Supply chain analytics covering commodity availability, stock status, "
            "stock-out trends, consumption, and logistics performance."
        ),
        "products": [
            {
                "id": "stock-status",
                "title": "Stock Status Dashboard",
                "type": "Dashboard",
                "status": "Prototype",
                "description": (
                    "Stock on hand, months of stock, stock availability, and "
                    "facility-level commodity status."
                ),
                "url": "/superset/dashboard/9/?standalone=1",
            },
            {
                "id": "stockout-trends",
                "title": "Stock-out Trends",
                "type": "Dashboard",
                "status": "Coming soon",
                "description": (
                    "Stock-out frequency, duration, affected commodities, and "
                    "district-level trends."
                ),
                "url": None,
            },
            {
                "id": "consumption-analysis",
                "title": "Consumption Analysis",
                "type": "Report",
                "status": "Coming soon",
                "description": (
                    "Consumption trends, reporting patterns, and commodity usage "
                    "over time."
                ),
                "url": None,
            },
            {
                "id": "facility-reporting",
                "title": "Facility Reporting Completeness",
                "type": "Indicator",
                "status": "Coming soon",
                "description": (
                    "Reporting completeness and timeliness across facilities and districts."
                ),
                "url": None,
            },
        ],
    },

    "ncmis": {
        "name": "Case Management",
        "badge": "NCMIS",
        "description": (
            "Case management analytics covering services, referrals, GBV/OVC "
            "indicators, client support workflows, and custom reports."
        ),
        "products": [
            {
                "id": "case-management-overview",
                "title": "Case Management Overview",
                "type": "Dashboard",
                "status": "Coming soon",
                "description": (
                    "Case volumes, services provided, case status, and programme-level "
                    "summary indicators."
                ),
                "url": None,
            },
            {
                "id": "referrals-dashboard",
                "title": "Referrals Dashboard",
                "type": "Dashboard",
                "status": "Coming soon",
                "description": (
                    "Referrals, completion status, service points, and referral outcomes."
                ),
                "url": None,
            },
            {
                "id": "gbv-ovc-indicators",
                "title": "GBV/OVC Service Indicators",
                "type": "Indicator set",
                "status": "Coming soon",
                "description": (
                    "Indicator catalogue for GBV, OVC, child protection, and case "
                    "management service indicators."
                ),
                "url": None,
            },
            {
                "id": "custom-reports",
                "title": "Custom Reports",
                "type": "Report",
                "status": "Coming soon",
                "description": (
                    "Custom reporting area for MGYSD operational and programme-specific "
                    "reporting needs."
                ),
                "url": None,
            },
        ],
    },

    "quality-improvement": {
        "name": "Quality Improvement",
        "badge": "CQI",
        "description": (
            "Quality improvement analytics covering improvement projects, service "
            "quality indicators, performance gaps, action plans, and CQI monitoring."
        ),
        "products": [
            {
                "id": "cqi-overview",
                "title": "CQI Overview Dashboard",
                "type": "Dashboard",
                "status": "Coming soon",
                "description": (
                    "Overview of CQI projects, performance gaps, improvement actions, "
                    "and progress against selected service quality indicators."
                ),
                "url": None,
            },
            {
                "id": "action-plan-tracker",
                "title": "Action Plan Tracker",
                "type": "Report",
                "status": "Coming soon",
                "description": (
                    "Tracks CQI action plans, responsible teams, implementation status, "
                    "and follow-up timelines."
                ),
                "url": None,
            },
            {
                "id": "indicator-performance",
                "title": "Indicator Performance Monitoring",
                "type": "Indicator",
                "status": "Coming soon",
                "description": (
                    "Monitors selected quality indicators across facilities, districts, "
                    "and reporting periods."
                ),
                "url": None,
            },
        ],
    },

    "laboratory": {
        "name": "Laboratory",
        "badge": "Lab",
        "description": (
            "Laboratory analytics covering test volumes, turnaround time, sample flow, "
            "results availability, and laboratory service performance."
        ),
        "products": [
            {
                "id": "lab-performance-overview",
                "title": "Laboratory Performance Overview",
                "type": "Dashboard",
                "status": "Coming soon",
                "description": (
                    "Summary of laboratory testing volumes, turnaround time, result "
                    "availability, and facility-level laboratory performance."
                ),
                "url": None,
            },
            {
                "id": "tat-monitoring",
                "title": "Turnaround Time Monitoring",
                "type": "Indicator",
                "status": "Coming soon",
                "description": (
                    "Monitors sample collection, testing, result approval, and result "
                    "return timelines across laboratory workflows."
                ),
                "url": None,
            },
            {
                "id": "sample-flow",
                "title": "Sample Flow and Results Tracking",
                "type": "Report",
                "status": "Coming soon",
                "description": (
                    "Tracks sample movement, pending results, rejected samples, and "
                    "result availability across facilities and laboratories."
                ),
                "url": None,
            },
        ],
    },

    "surveillance": {
        "name": "Surveillance",
        "badge": "Public Health",
        "description": (
            "Surveillance analytics covering case reporting, alerts, event monitoring, "
            "trends, and public health response indicators."
        ),
        "products": [
            {
                "id": "surveillance-overview",
                "title": "Surveillance Overview Dashboard",
                "type": "Dashboard",
                "status": "Coming soon",
                "description": (
                    "Overview of surveillance reporting, disease/event trends, alerts, "
                    "and response monitoring indicators."
                ),
                "url": None,
            },
            {
                "id": "alerts-and-events",
                "title": "Alerts and Events Monitoring",
                "type": "Report",
                "status": "Coming soon",
                "description": (
                    "Tracks reported alerts, public health events, verification status, "
                    "and response actions."
                ),
                "url": None,
            },
            {
                "id": "case-reporting-trends",
                "title": "Case Reporting Trends",
                "type": "Indicator",
                "status": "Coming soon",
                "description": (
                    "Monitors case reporting trends, reporting completeness, geographic "
                    "distribution, and changes over time."
                ),
                "url": None,
            },
        ],
    },
}