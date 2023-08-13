import streamlit as st
import pandas as pd
import numpy as np

st.title("--------------------------------EnergyLo------------------------------")
st.header("Decentralized Transaction Ledger")

# df = pd.DataFrame(
#    np.random.randn(10, 5),
#    columns=('Seller', 'Buyer', ''))
data = {
    'Seller' : ["1fusyk3g87rpgn04mt2t6p4up01t5xvs",
"ody48dj6ondshmuoydspifrfg6ku8hyg",
"t26r0mq5aex0z2qqh8729zlnkkjje36i",
"geuhbfrmvo1lqk0qvithxyi5orb7uwop",
"coxky5pcibp3mw7bvilvu5tg2sdd5v5u",
"fbpaygi3d0ypeo7vxfrzxaxpiqiz7o49",
"3ggtdfh4t9t0lxe8n28n4o5tjnac5znf",
"sa5mb42nw3pfk0f7nr1aj0jl7llznjdz",
"zcf18vy3bpr0rkxg8b2o8ogf8d91jzo4",
"jd4q3g8circr4ugc6zoetwx5kiccq6y8","1fusyk3g87rpgn04mt2t6p4up01t5xvs",
"ody48dj6ondshmuoydspifrfg6ku8hyg",
"t26r0mq5aex0z2qqh8729zlnkkjje36i",
"geuhbfrmvo1lqk0qvithxyi5orb7uwop",
"coxky5pcibp3mw7bvilvu5tg2sdd5v5u",
"fbpaygi3d0ypeo7vxfrzxaxpiqiz7o49",
"3ggtdfh4t9t0lxe8n28n4o5tjnac5znf",
"sa5mb42nw3pfk0f7nr1aj0jl7llznjdz",
"zcf18vy3bpr0rkxg8b2o8ogf8d91jzo4",
"jd4q3g8circr4ugc6zoetwx5kiccq6y8"
], 
'Buyer' : ["gninw5wsl0loxruu3w07q2wxvcxeaoii",
"1mata6smulztm640h7g29e8l9gp08eva",
"wkjlrca6koso1ek9hkgjvza3ckht8c9y",
"z4wdzl8lwh62urui49qhdkcya8npdnb6",
"0vfk4kmonne9t2axhd96eoc0kxupx8pu",
"9cystu3p38dbgt377mb9f51zxbl7ipaq",
"xudcaeycsgjiabklg87ixv7vh8c3ftk0",
"6f9z27tpwvimfohefhfokkwk3legz7it",
"jqyehkrs07a2both3sykij4sc8j050r2",
"ukw77z7pp1yi9ziwhg48referj8keyog",
"1fusyk3g87rpgn04mt2t6p4up01t5xvs",
"ody48dj6ondshmuoydspifrfg6ku8hyg",
"t26r0mq5aex0z2qqh8729zlnkkjje36i",
"geuhbfrmvo1lqk0qvithxyi5orb7uwop",
"coxky5pcibp3mw7bvilvu5tg2sdd5v5u",
"fbpaygi3d0ypeo7vxfrzxaxpiqiz7o49",
"3ggtdfh4t9t0lxe8n28n4o5tjnac5znf",
"sa5mb42nw3pfk0f7nr1aj0jl7llznjdz",
"zcf18vy3bpr0rkxg8b2o8ogf8d91jzo4",
"jd4q3g8circr4ugc6zoetwx5kiccq6y8",
],
'Source':["rey5xcrrofduyfk98ke8vp5pjvf2rfe7",
"93ijwaojzo31dxi077tzwwgyyd4shpcj",
"uzbcko1g660f690wbt6dwun5gsjtvv5s",
"99u82ksr5hr1kg9h2a7k04yrlu4780wx",
"qqesya2ewoet8lywpyhvr3yauysltnav",
"rij2a6c4okq3x4tsivmyzy4r6izv9bo6",
"qnoese8dcwdqgp18gs8cmfzc4g2js7x0",
"x4gy4oydxkcvvic06xgusuk2iiaaacjj",
"swy9er7ndp7dbf4oo6siktxd7fhbbu0w",
"ny99kbhem3x8u6txvid4qz2g1c8177mt",
"1fusyk3g87rpgn04mt2t6p4up01t5xvs",
"ody48dj6ondshmuoydspifrfg6ku8hyg",
"t26r0mq5aex0z2qqh8729zlnkkjje36i",
"geuhbfrmvo1lqk0qvithxyi5orb7uwop",
"coxky5pcibp3mw7bvilvu5tg2sdd5v5u",
"fbpaygi3d0ypeo7vxfrzxaxpiqiz7o49",
"3ggtdfh4t9t0lxe8n28n4o5tjnac5znf",
"sa5mb42nw3pfk0f7nr1aj0jl7llznjdz",
"zcf18vy3bpr0rkxg8b2o8ogf8d91jzo4",
"jd4q3g8circr4ugc6zoetwx5kiccq6y8",
], 
'FalseValue of Seller': [8.866049535367228,
6.524337360724005,
4.640430531753166,
6.691666168602229,
5.78593501040367,
2.5966455682366396,
9.166012066239318,
0.5409239540646271,
6.048447952602867,
0.6219653076604037,
8.866049535367228,
6.524337360724005,
4.640430531753166,
6.691666168602229,
5.78593501040367,
2.5966455682366396,
9.166012066239318,
0.5409239540646271,
6.048447952602867,
0.6219653076604037,
],
'ActualValue of Buyer':[9.30050527476798,
0.1808349691233846,
5.158286883824173,
1.0865748188387248,
3.3516018713333517,
7.45746214613329,
2.67611231052351,
5.278184135775649,
8.398830983394244,
9.460423700919904,
8.866049535367228,
6.524337360724005,
4.640430531753166,
6.691666168602229,
5.78593501040367,
2.5966455682366396,
9.166012066239318,
0.5409239540646271,
6.048447952602867,
0.6219653076604037,
]
}

df = pd.DataFrame(data)  

st.table(df)