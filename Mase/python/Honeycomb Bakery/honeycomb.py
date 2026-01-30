cupcakes = 0.40
macarons = 0.50
cheesecake = 0.70

cakes_amount = int(input("How many cupcakes do you plan to sell? "))
macarons_amount = int(input("How many macarons do you plan to sell? "))
cheesecake_amount = int(input("How many cheesecakes do you plan to sell? "))


cakes_answer = cakes_amount * cupcakes
macaron_answer = macarons_amount * macarons
cheesecake_answer = cheesecake_amount * cheesecake

answer = (f"You ordered £{cakes_answer:.2f} raised from cakes, £{macaron_answer:.2f} from macarons and £{cheesecake_answer:.2f} raised from cheesecakes ")
print(answer)
