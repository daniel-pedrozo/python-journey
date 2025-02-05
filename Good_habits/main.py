
name: str = "daniel"
age: int = 19
funds: float = 5.100
has_id: bool = True

def enter_bar(has_id: bool) -> None:
    if has_valid_id(has_id):
        print("yep you have one id!")
    else:
        print("not id")

def has_valid_id(has_id: bool) -> bool:
    return has_id

def main(has_id) -> None:
    enter_bar(has_id)
    
if __name__ == "__main__":
    main(has_id)