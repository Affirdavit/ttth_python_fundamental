def main():
    x = int(input("Nhap chieu dai: "))
    y = int(input("Nhap chieu rong: "))
    perimeter = lambda x, y: (x + y) * 2
    area = lambda x, y: x * y
    print(f"Chu vi: {perimeter(x, y)}")
    print(f"Dien tich: {area(x, y)}")

if __name__ == '__main__':
    main()