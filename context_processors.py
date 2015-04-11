def site_settings_processor(request):
	context_dictionary = {
		'root_url': 'www.SurgeSite.com',
		'admin_name': 'superuser',
		'company_name': 'SurgeSite Web Design & Web Development',
		'company_name_short': 'SurgeSite', #used in Title tag
		'logo_file_name': 'images/surgesite_logo.png',
		'site_email': 'contact@SurgeSite.com',
		# !!!! important !!!! contact.html has ascii email addresses, must edit those manually
		'company_phone_text': '',
		'company_phone_link': '16024299029',
		'homepage_title': 'SurgeSite, Tempe Web Design and Development',
		'blog_home_title': 'Blog Home - SurgeSite',
		'homepage_meta_description': 'SurgeSite develops and designs small business website solutions. All websites are hand-coded and maintained for your business\'s needs.',
		'navbar_link1_name': '/#portfolio',
		'navbar_link1_text': 'PORTFOLIO',
		'navbar_link2_name': '/#services',
		'navbar_link2_text': 'SERVICES',
		'navbar_link3_name': '/#about',
		'navbar_link3_text': 'ABOUT',
		'navbar_link4_name': '/blog',
		'navbar_link4_text': 'BLOG',
		'navbar_link5_name': '/#contact',
		'navbar_link5_text': 'CONTACT',
	}
	return(context_dictionary)