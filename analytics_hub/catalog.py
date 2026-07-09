ANALYTICS_HUB_SYSTEMS = {
    "ihris": {
        "name": "iHRIS",
        "badge": "HRH",
        "description": (
            "Human resources for health analytics covering staffing levels, "
            "cadres, facilities, workforce distribution, and HRH reporting."
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
                "url": "/superset/dashboard/world_health/?standalone=1",
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
        "name": "eLMIS",
        "badge": "Supply Chain",
        "description": (
            "Supply chain analytics covering commodity availability, stock status, "
            "stock-out trends, consumption, and logistics performance."
        ),
        "products": [
            {
                "id": "stock-status",
                "title": "Stock Status Dashboard",
                "type": "Dashboard",
                "status": "Coming soon",
                "description": (
                    "Stock on hand, months of stock, stock availability, and "
                    "facility-level commodity status."
                ),
                "url": None,
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
        "name": "NCMIS",
        "badge": "MGYSD",
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
}