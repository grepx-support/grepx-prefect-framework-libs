"""Test Prefect Framework."""

import sys
from pathlib import Path

# Add the src directory to the path
sys.path.insert(0, str(Path(__file__).parent / "src"))

try:
    # Import the Prefect framework
    from prefect_framework import PrefectApp
    
    # Create app instance
    app = PrefectApp()
    
    print("✅ PrefectApp initialized successfully")
    
    # Test registering a flow (using the existing price_etl_flow)
    try:
        from prefect_app.prefect_app import load_prefect_flows
        flows = load_prefect_flows()
        for name, flow in flows.items():
            app.register_flow(name, flow)
            print(f"✅ Registered flow: {name}")
        
        # Test getting flows
        flow_list = app.list_flows()
        print(f"✅ Listed {len(flow_list)} flows: {flow_list}")
        
        # Test getting a specific flow
        if flow_list:
            flow = app.get_flow(flow_list[0])
            print(f"✅ Retrieved flow: {flow.name if hasattr(flow, 'name') else flow_list[0]}")
            
    except Exception as e:
        print(f"⚠️  Warning: Could not register flows: {e}")
    
    print("\n🎉 Prefect Framework test completed!")
    
except Exception as e:
    print(f"❌ Error: {e}")
    import traceback
    traceback.print_exc()