import pickle

data=[["MAFFT","Unsettled","7.304",""],
      ["Gblocks","Unsettled","0.91b",""],
      ["PartitonFinder (nucleotide)","Unsettled","1.1.1",""],
      ["PartitonFinder (protein)","Unsettled","1.1.1",""],
      ["pal2nal","Unsettled","14.0",""],
      ["tbl2asn","Unsettled","1.0",""],
      ["PRANK","Unsettled","v.140603",""]
      ]

with open("plugins.pickle","wb") as f:
    pickle.dump(data,f)
