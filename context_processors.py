def site_settings_processor(request):
	context_dictionary = {
		# 'root_url': 'jpark.pythonanywhere.com',
		'root_url': '127.0.0.1:8000',
		'admin_name': 'superuser',
		'company_name': 'SurgeSite Web Design & Development',
		'logo_file_name': 'images/surgesite_logo.png',
		'site_email': 'jaredjamespark@gmail.com',
		# if email changes, update misc_pages/email.html
		'company_phone_text': '602-429-9029',
		'company_phone_link': '16024299029',
		'yelp_id': 'barefoot-pools-pool-service-and-repair-phoenix',
		'editable_profile_field_label_list': ['image', 'address', 'city', 'zipcode', 'phone'],
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