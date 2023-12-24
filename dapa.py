from libs.yutix import *

class Cek:
	def __init__(self,raw,out):
		self.raw = raw.strip()
		self.out = out
		self.dei = 0
		self.go()
	
	def go(self):
		try:
			url = self.get_url()
			moz = "https://scanbacklinks.com/check-dapa"
			ses = req.session()
			key = bs(ses.get(moz,verify=False,timeout=15).text,"html.parser").find("input",{"name":"_csrf-frontend"})["value"]
			raw = ses.post(moz,data={"_csrf-frontend":key,"CheckForm[site]":f"http://{url}"},verify=False,timeout=15).text
			sup = bs(raw,"html.parser")
			row = req.post("https://www.useotools.com/google-index-checker/output",data={"submit":"Submit","url":f"http://{url}"},verify=False,timeout=10).text
			_DA = int(sup.find("div",{"class":"da"}).span.text.strip())
			_PA = int(sup.find("div",{"class":"pa"}).span.text.strip())
			
			if _DA > minda: da_color = green
			else: da_color = red
			if _PA > minpa: pa_color = green
			else: pa_color = red
			
			if _DA > minda and _PA > minpa:
				if self.out:
					open(self.out,"a").write(f"╔═[ {self.raw}\n╚═══> DA: {_DA} ~ PA: {_PA}\n\n")
				
			print(f" {bold}{red}╔═[{reset} {url.title()}{reset}")
			print(f" {bold}{red}╚═══>{reset} {da_color}DA: {_DA} {reset}~ {pa_color}PA: {_PA} {reset}\n")
			
		except Exception as err:
			if self.dei == 7:
				print(f" {bold}{red}╔═[{reset} {url.title()}{reset}")
				print(f" {bold}{red}╚═══>{reset}{dim} {err}{reset}\n")
			else:
				self.dei += 1
				self.go()
	
	def get_url(self):
		res = []
		for i in self.raw.split():
			raw = tldextract.extract(i)
			if raw.suffix:
				res.append(".".join(filter(None,raw)))
		if res:
			return res[0]
		else:
			print(f" {bold}{red}╔═[{reset} {self.raw}{reset}")
			print(f" {bold}{red}╚═══>{reset}{dim} file not found or url you entered is invalid{reset}\n")
			exit()

def main():
	global minda, minpa
	
	parser = argparse.ArgumentParser(prog=" DapaScan",add_help=True,usage="\r Usage: ./dapa.py [--da DA] [--pa PA] [-o FILE] [-h] TARGET")
	parser.add_argument("target", help="url or file contain urls")
	parser.add_argument("-o", "--out", help="Save results to FILE", metavar="FILE")
	parser.add_argument("--da", default=0, type=int, help="Set minimun DA")
	parser.add_argument("--pa", default=0, type=int, help="Set minimun PA")
	parser._positionals.title = " Positional Arguments"
	parser._optionals.title = " Optional Arguments"
	args = parser.parse_args()
	
	try: urls = open(args.target).read().splitlines()
	except FileNotFoundError: urls = [args.target]
	
	minda += args.da
	minpa += args.pa
	
	for i in urls:
		Cek(i,args.out)

header("Domain Authority & Page Authority Checker - v1.0")
minda = 0
minpa = 0

if __name__=="__main__":
	main()