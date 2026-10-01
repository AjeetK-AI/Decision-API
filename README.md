Decision API 
Gmail Agent -> Decison API-> Decision Engine -> Execution 

What it will do?
Mail Context Check + Desired Action -> DECISION-> Execute 

Agent Check Gmail for Customer Complaint ->(Sends to Decision API) ->Execute 

Architecture 

                         Gmail User 

                         Gmail Agent
                           Read Email 
                           Understand 
                           Execute Action

                           DECISION API
                           Fast API

            Validates     Decision Engine     Policy Engine 
            Pydantic 

                        
                           LLM Layer 

                           Structured Decision 

                           Decision Response 

                           Gmail Agent 

                           Gmail API 


3 LAYERS - Agent Layer /Gmail Agent -> DECISION API (Context,Policy What agents should do) -> Execute 
