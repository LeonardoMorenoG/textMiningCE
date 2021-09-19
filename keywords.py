import argparse
from os import listdir
import os
import re
import pandas as pd


myParser = argparse.ArgumentParser(description="Given a folder with papers, returns the normalized count of the selected keywords")

#Add the arguments
myParser.add_argument("-pdfs",metavar="PDFs folder",type=str,help="Path to the input PDFs",required=True)

#import the arguments
args = myParser.parse_args()

#Functions
def pdf2txt(path):
	os.system("pdf2txt.py "+path+" > paper.txt")

def removePunctuation(line):
	return re.sub(r'[^\w\s]','',line)

def txt2dict():
	textDict = {}
	with open("paper.txt","r") as fr:
		for line in fr:
			line = removePunctuation(line.strip('\n'))
			line = line.split(' ')
			for word in line:
				word = word.lower()
				if word in textDict:
					textDict[word] += 1
				else:
					textDict[word] = 1
	return textDict

def norm(times,elements):
	"""
	Normalizes the count of a keyword given the number of times that the words appear (times) and the number of words used in the search (elements)
	"""
	if elements > 0:
		return times/elements
	return 0

def dict2keywords(textDict):
	mitigation = 0
	if "mitigation" in textDict:
		mitigation += textDict["mitigation"]
	adaptation = 0
	if "adaptation" in textDict:
		adaptation += textDict["adaptation"]
	ghg = 0
	ghgWordCounter = 0 
	if ("greenhouse" in textDict and "effect" in textDict):
		ghg += min([textDict["greenhouse"],textDict["effect"]])
		ghgWordCounter += 1
	if ("greenhouse" in textDict and "gas" in textDict):
		ghg += min([textDict["greenhouse"],textDict["gas"]])
		ghgWordCounter += 1
	if ("greenhouse" in textDict and "emission" in textDict):
		ghg += min([textDict["greenhouse"],textDict["emission"]])
		ghgWordCounter += 1
	if ("global" in textDict and "warming" in textDict):
		ghg += min([textDict["global"],textDict["warming"]])
		ghgWordCounter += 1
	if "ghg" in textDict:
		ghg += textDict["ghg"]
		ghgWordCounter += 1
	waste = 0
	wasteWordCounter = 0
	if "waste" in textDict:
		waste += textDict["waste"]
		wasteWordCounter += 1
		if "reduce" in textDict:
			waste +=  textDict["reduce"]
			wasteWordCounter += 1
		if "reuse" in textDict:
			waste += textDict["reuse"]
			wasteWordCounter += 1
		if "recycle" in textDict:
			waste += textDict["recycle"]
			wasteWordCounter += 1
		if "recover" in textDict:
			waste += textDict["recover"]
			wasteWordCounter += 1
	product = 0
	productWordCounter = 0
	if "product" in textDict:
		product += textDict["product"]
		productWordCounter += 1
		if "rethink" in textDict:
			product += textDict["rethink"]
			productWordCounter += 1
		if ("eco" in textDict and "design" in textDict):
			product += min([textDict["eco"],textDict["design"]])
			productWordCounter += 1
		if ("eco" in textDict and "innovation" in textDict):
			product += min([textDict["eco"],textDict["innovation"]])
			productWordCounter += 1 
		if "redesign" in textDict:
			product += textDict["redesign"]
			productWordCounter += 1
		if "ecolabelling" in textDict:
			product += textDict["ecolabelling"]
			productWordCounter += 1
		if "refurbishment" in textDict:
			product += textDict["refurbishment"]
			productWordCounter += 1
		if "remanufacture" in textDict:
			product += textDict["remanufacture"]
			productWordCounter += 1
	resource = 0
	resourceWordCounter = 0
	if "resource" in textDict:
		resource += textDict["resource"]
		resourceWordCounter += 1
		if "reduce" in textDict:
			resource += textDict["reduce"]
			resourceWordCounter += 1
		if ("raw" in textDict and "material" in textDict):
			resource += min([textDict["raw"],textDict["material"]])
			resourceWordCounter += 1
		if "renewable" in textDict:
			resource += textDict["renewable"]
			resourceWordCounter += 1
		if ("bio"  in textDict and "improved" in textDict):
			resource += min([textDict["bio"],textDict["improved"]])
			resourceWordCounter += 1
		if ("bio-based" in textDict and "materials" in textDict):
			resource += min([textDict["bio-based"],textDict["materials"]])
			resourceWordCounter += 1
		if ("water" in textDict and "treatment" in textDict):
			resource += min([textDict["water"],textDict["treatment"]])
			resourceWordCounter += 1
		if "optimization" in textDict:
			resource += textDict["optimization"]
			resourceWordCounter += 1
		if "replacement" in textDict:
			resource += textDict["replacement"]
			resourceWordCounter += 1
		if "efficiency"  in textDict:
			resource += textDict["efficiency"]
			resourceWordCounter += 1
	supplyChain = 0
	supplyChainWordCounter = 0
	if ("supply" in textDict and "chain" in textDict):
		supplyChain += min([textDict["supply"],textDict["chain"]])
		supplyChainWordCounter += 1
		if ("equipment" in textDict and "acquisitions" in textDict):
			supplyChain += min([textDict["equipment"],textDict["acquisitions"]])
			supplyChainWordCounter += 1
		if ("green" in textDict and "procurement" in textDict):
			supplyChain += min([textDict["green"],textDict["procurement"]])
			supplyChainWordCounter += 1
		if ("sustainable" in textDict and "infrastructure" in textDict):
			supplyChain += min([textDict["sustainable"],textDict["infrastructure"]])
			supplyChainWordCounter += 1
		if ("industrial" in textDict and "symbiosis" in textDict):
			supplyChain += min([textDict["industrial"],textDict["symbiosis"]])
			supplyChainWordCounter += 1
		if ("poly" in textDict and "generation" in textDict and "systems" in textDict):
			supplyChain += min([textDict["poly"],textDict["generation"],textDict["systems"]])
			supplyChainWordCounter += 1
		if "biochemical" in textDict:
			supplyChain += textDict["biochemical"]
			supplyChainWordCounter += 1
		if "upcycling" in textDict:
			supplyChain += textDict["upcycling"]
			supplyChainWordCounter += 1
		if ("extended" in textDict and "producer" in textDict and "responsibility" in textDict):
			supplyChain += min([textDict["extended"],textDict["producer"],textDict["responsibility"]])
			supplyChainWordCounter += 1
		if "downcycling" in textDict:
			supplyChain += textDict["downcycling"]
			supplyChainWordCounter += 1
		if "logistics" in textDict:
			supplyChain += textDict["logistics"]
			supplyChainWordCounter += 1
	clientsCommunity = 0
	clientsCommunityWordsCounter = 0
	if "clients" in textDict or "community" in textDict:
		if "clients" in textDict:
			clientsCommunity += textDict["clients"]
			clientsCommunityWordsCounter += 1
		if "community" in textDict:
			clientsCommunity += textDict["community"]
			clientsCommunityWordsCounter += 1
		if "society" in textDict:
			clientsCommunity += textDict["society"]
			clientsCommunityWordsCounter += 1
		if ("responsible" in textDict and "consumption" in textDict):
			clientsCommunity += min([textDict["responsible"],textDict["consumption"]])
			clientsCommunityWordsCounter += 1
		if "costumers" in textDict:
			clientsCommunity += textDict["costumers"]
			clientsCommunityWordsCounter += 1
		if ("product" in textDict and "service" in textDict and "system" in textDict):
			clientsCommunity += min([textDict["product"],textDict["service"],textDict["system"]])
			clientsCommunityWordsCounter += 1
	cement = 0
	if "cement" in textDict:
		cement += textDict["cement"]
	steel = 0
	if "steel" in textDict:
		steel += textDict["steel"]
	aluminium = 0
	if "aluminium" in textDict:
		aluminium += textDict["aluminium"]
	plastics = 0
	if "plastics" in textDict:
		plastics += textDict["plastics"]
	food = 0
	if "food" in textDict:
		food += textDict["food"]
	ods13 = 0
	try:
		ods13 += min([textDict["sustainable"],textDict["development"],textDict["goal"],textDict["13"]])
		ods13 += min([textDict["SDG"],textDict["13"]])
	except:
		ods13 += 0
	return [mitigation,adaptation,norm(ghg,ghgWordCounter),norm(waste,wasteWordCounter),norm(product,productWordCounter),norm(resource,resourceWordCounter),\
	norm(supplyChain,supplyChainWordCounter),norm(clientsCommunity,clientsCommunityWordsCounter),cement,steel,aluminium,plastics,food,ods13]

#__main__
df = pd.DataFrame(columns=["Paper","Mitigation","Adaptation","Greenhouse gases","Waste","Product","Resource","Supply Chain","Clients and Community","Cement","Steel",\
	"Aluminium","Plastics","Food","ODS 13"])
i = 0
for f in listdir(args.pdfs):
	if ".pdf" in f:
		path = args.pdfs+"/"+f
		pdf2txt(path)
		textDict = txt2dict()
		row = [f]+dict2keywords(textDict)
		#print(row)
		df.loc[i] = row
		i += 1
		if i%10 == 0:
			print("Processing paper number "+str(i))
#print(df)
df.to_csv("keywordCount.normalized.csv",header=True,index=False,sep='\t')
		