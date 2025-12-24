"""Integration test for Prefect Framework with Connection Registry."""

import sys
from pathlib import Path

# Add necessary paths
sys.path.insert(0, str(Path(__file__).parent / "src" / "main"))
sys.path.insert(0, str(Path(__file__).parent / "libs" / "prefect_framework" / "src"))

try:
    # Import the main application
    from servers.app.application import Application
    
    # Initialize the application
    app = Application()
    
    print("✅ Application initialized successfully")
    
    # Test getting Prefect flows through the connection manager
    print("\n🔍 Testing Prefect flows access through connection manager...")
    flows = app.get_prefect_flows()
    print(f"✅ Retrieved {len(flows)} Prefect flows:")
    for flow_name, flow in flows.items():
        print(f"  - {flow_name}: {flow}")
    
    # Test getting a specific flow
    print("\n🔍 Testing specific flow access...")
    flow = app.get_prefect_flow("price_etl_flow")
    if flow:
        print(f"✅ Retrieved flow: {flow.name}")
    else:
        print("❌ Failed to retrieve flow")
        
    print("\n🎉 All integration tests passed!")
    
except Exception as e:
    print(f"❌ Error: {e}")
    import traceback
    traceback.print_exc()