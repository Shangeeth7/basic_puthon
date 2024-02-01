# import httpx
# from prefect import flow, get_run_logger


# @flow
# def get_repo_info(repo_name: str = "PrefectHQ/prefect"):
#     url = f"https://api.github.com/repos/{repo_name}"
#     response = httpx.get(url)
#     response.raise_for_status()
#     repo = response.json()
#     logger = get_run_logger()
#     logger.info("%s repository statistics 🤓:", repo_name)
#     logger.info(f"Stars 🌠 : %d", repo["stargazers_count"])
#     logger.info(f"Forks 🍴 : %d", repo["forks_count"])
#     print("Completed Prefect-flow with Logger")

# if __name__ == "__main__":
#     get_repo_info()


def fizzbuzz(n):
    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

# Example usage:
fizzbuzz(20)
