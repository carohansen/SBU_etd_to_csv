import xml.etree.ElementTree as ET
import csv
import glob
import re
forCSV =[]
forCSV.append(['authorname', 'title', 'dept', 'keywords', 'pages', 'abstract', 'advisorname', 'committeemembers', 'publishing_option', 'embargocode', 'third_party_search', 'delayed_release_date', 'complete_date', 'accept_date', 'filename'])

for file in glob.glob('*.xml'):
	print(file)
	tree = ET.parse(file)
	root = tree.getroot()

	for item in root.iter('DISS_advisor'):
		advisorsurname= item.find('DISS_name/DISS_surname').text
		advisorfirstname= item.find('DISS_name/DISS_fname').text
		advisormiddlename= item.find('DISS_name/DISS_middle').text
		advisorname= advisorsurname, advisorfirstname, advisormiddlename

	for item in root.iter('DISS_author'):
		authorsurname= item.find('DISS_name/DISS_surname').text
		authorfirstname= item.find('DISS_name/DISS_fname').text
		authormiddlename= item.find('DISS_name/DISS_middle').text
		authorsuffix= item.find('DISS_name/DISS_suffix').text
		authorname= authorsurname, authorfirstname, authormiddlename, authorsuffix

	for item in root.iter('DISS_content'):
		filename= item.find('DISS_binary').text

	combined_committee_members= ""

	for item in root.iter('DISS_cmte_member'):
	    comtesurname= item.find('DISS_name/DISS_surname').text
	    comtefirstname= item.find('DISS_name/DISS_fname').text
	    fullname= str((comtesurname, comtefirstname))
	    combined_committee_members += fullname

	for item in root.iter('DISS_description'):
		accept_date= item.find('DISS_dates/DISS_accept_date').text
		complete_date= item.find('DISS_dates/DISS_comp_date').text
		dept= item.find('DISS_institution/DISS_inst_contact').text
		keywords= item.find('DISS_categorization/DISS_keyword').text
		pages= item.get('page_count') + " pages"
		title= item.find('DISS_title').text

	combined_abstracts= ""

	for item in root.iter("DISS_para"):
	    combined_abstracts += re.sub('\t', '', item.text)

	for item in root.iter("DISS_repository"):
		delayed_release_date= item.find('DISS_delayed_release').text

	for item in root.iter('DISS_submission'):
		embargocode= item.get('embargo_code')
		publishing_option= item.get('publishing_option')
		third_party_search= item.get('third_party_search')

	forCSV.append([authorname, title, dept, keywords, pages, combined_abstracts, advisorname, combined_committee_members, publishing_option, embargocode, third_party_search, delayed_release_date, complete_date, accept_date, filename])

	with open('outputFile.csv', 'w', newline='') as csvfile:
		wr= csv.writer(csvfile, delimiter=',')
		wr.writerows(forCSV)

