sec = int(input('введите количество секунд:' ))

if sec < 60:
    print(f'00:00:{sec}')
elif sec < 3600:
    print(f"00:{sec // 60}:{sec % 60}")
else:
    print(f"{sec // 3600}:{sec % 3600}//60:{sec % 60}")