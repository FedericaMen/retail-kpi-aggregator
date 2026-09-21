# ==============================================================================
# RETAIL MULTI-STORE KPI AGGREGATOR
# Author: Federica
# Description: Automated script for aggregating multi-store retail sales data
# ==============================================================================

def calculate_store_kpis(store_name, total_sales, transaction_count):
    """
    Calculates key metrics for an individual store location.
    """
    if transaction_count == 0:
        average_order_value = 0.0
    else:
        average_order_value = total_sales / transaction_count
        
    return {
        "store": store_name,
        "total_sales": total_sales,
        "transaction_count": transaction_count,
        "average_order_value": round(average_order_value, 2)
    }

# Simulated data feed from retail locations (e.g., extracted from POS/ERP exports)
store_data_feed = [
    {"store": "A Store", "sales": 4500.50, "transactions": 180},
    {"store": "B Store", "sales": 6200.00, "transactions": 210},
    {"store": "C Store", "sales": 7800.80, "transactions": 290}
]

def main():
    print("--- STARTING RETAIL DATA AGGREGATION ---")
    
    summary_report = []
    total_group_sales = 0.0
    total_group_transactions = 0

    # Processing sales data for each store location
    for store in store_data_feed:
        kpis = calculate_store_kpis(store["store"], store["sales"], store["transactions"])
        summary_report.append(kpis)
        
        total_group_sales += store["sales"]
        total_group_transactions += store["transactions"]

    # Output store-level performance breakdown
    print("\nLOCATION PERFORMANCE BREAKDOWN:")
    for item in summary_report:
        print(
            f"• {item['store']}: €{item['total_sales']:,.2f} Sales | "
            f"{item['transaction_count']} Transactions | "
            f"AOV: €{item['average_order_value']}"
        )
        
    group_aov = (
        total_group_sales / total_group_transactions 
        if total_group_transactions > 0 
        else 0.0
    )
    
    print("\n--- GROUP EXECUTIVE SUMMARY ---")
    print(f"Total Group Revenue: €{round(total_group_sales, 2):,.2f}")
    print(f"Total Group Transactions: {total_group_transactions}")
    print(f"Overall Average Order Value (AOV): €{round(group_aov, 2):,.2f}")

if __name__ == "__main__":
    main()
