import requests
import hashlib
import sys  # noqa: F401 
from  postq import call



def request_bytes(query:str):
 url: str ="https://api.pwnedpasswords.com/range/" + query
 res = requests.get(url)
 if res.status_code!=200:
      raise RuntimeError(f"an error {res.status_code} has occured")
 return res

def get_count(hashes,rest):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for _,count in hashes:
       if (_ == rest) :
        return count
    return 0


        




def check_api(password) -> str:
    passwd = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
      
    kanom,rest = passwd[:5],passwd[5:]
    response= request_bytes(kanom)
    return get_count(response,rest)
    

def main(args):

    for _ in args:
        l=len(_)
        cc=check_api(_)
        if cc:
            print(f"YOUR PASS : {_} HAS BEEN BREACHED {cc} TIMES !")
            print(f"YOU MUST UPDATE {_} WITH ONE OF THE FOLLOWING :")
            call(l)
            print("the longer the pass you set , the better")
        else:
            print(f"good News ! your pass {_} is safe for now ")
            print(f"you may consider updating : {_} with one of the post quantum passwords for maximum safety")
            call(l)
            print("the longer the pass you set , the better")




    
if __name__ == '__main__':
  sys.exit(main(sys.argv[1:])) #wiwi sleep()





