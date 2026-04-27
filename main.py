import subprocess
from datetime import datetime, timedelta

def main():
    print("=" * 40)
    print("   win-scheduler")
    print("=" * 40)
    print()

    while True:
        time_input = input("ЧЧ:ММ: ").strip()
        
        try:
            target_time = datetime.strptime(time_input, "%H:%M")
        except ValueError:
            print("ЧЧ:ММ (пример - 23:30)\n")
            continue

        now = datetime.now()
        target = now.replace(
            hour=target_time.hour,
            minute=target_time.minute,
            second=0,
            microsecond=0
        )

        if target <= now:
            target += timedelta(days=1)

        seconds = int((target - now).total_seconds())

        print()
        print(f"текущее время:      {now.strftime('%H:%M:%S')}")
        print(f"выключение в:       {target.strftime('%H:%M')}")
        print(f"осталось секунд:    {seconds}  ({seconds // 3600}ч {(seconds % 3600) // 60}м {seconds % 60}с)")
        print()

        confirm = input("запустить? (д/н): ").strip().lower()
        if confirm in ("д", "y", "да", "yes", ""):
            subprocess.run(["shutdown", "-s", "-t", str(seconds)], check=True)
            print()
            print(f"✓ выключится в {target.strftime('%H:%M')}.")
            print("  отменить - shutdown -a")
            break
        else:
            print("отменено\n")

    print()
    input("enter...")

if __name__ == "__main__":
    main()