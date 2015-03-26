def site_settings_processor(request):
	context_dictionary = {
		'root_url': 'www.SurgeSite.com',
		'admin_name': 'superuser',
		'company_name': 'SurgeSite Web Design & Development',
		'logo_file_name': 'images/surgesite_logo.png',
		'site_email': 'contact@SurgeSite.com',
		# !!!! important !!!! contact.html has ascii email addresses, must edit those manually
		'company_phone_text': '',
		'company_phone_link': '16024299029',
		'meta_content': 'SurgeSite develops and designs meaningful web based business solutions. We build websites, web applications and execute data-driven pay-per-click campaigns.',
		'navbar_link1_name': '#portfolio',
		'navbar_link1_text': 'PORTFOLIO',
		'navbar_link2_name': '#services',
		'navbar_link2_text': 'SERVICES',
		'navbar_link3_name': '#about',
		'navbar_link3_text': 'ABOUT',
		'navbar_link4_name': '#contact',
		'navbar_link4_text': 'CONTACT',
	}
	return(context_dictionary)