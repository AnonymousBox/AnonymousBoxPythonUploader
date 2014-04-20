import MultipartPostHandler, urllib2, cookielib, json, ast 
def uploadeverything(params, files):
    cookies = cookielib.CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookies),
              MultipartPostHandler.MultipartPostHandler)
    paramstosend = params
    for i in range(len(files)):
        paramstosend["file"+str(i)] = open(files[i], "rb")
    paramstosend["temperature"] = str(ast.literal_eval(urllib2.urlopen("http://api.openweathermap.org/data/2.5/weather?q=amherst&units=imperial").read())['main']['temp'])
    print paramstosend
    opener.open("http://anonymousbox.herokuapp.com/post", paramstosend)
#   paramstosend = params
#   paramstosend["file"] = open(filename, "rb")
#   print paramstosend
#   cookies = cookielib.CookieJar()
#   opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookies), MultipartPostHandler.MultipartPostHandler)
#   opener.open("http://127.0.0.1:3000/post", paramstosend)




