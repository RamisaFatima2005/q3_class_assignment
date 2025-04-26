import streamlit as st

# --- OOP Classes ---
class Car:
    def __init__(self, brand, model, year, rate_per_day):
        self.brand = brand
        self.model = model
        self.year = year
        self.rate_per_day = rate_per_day
        self.available = True

    def display_info(self):
        return f"{self.brand} {self.model} ({self.year}) - Rate: {self.rate_per_day}/day"


class RentalCar(Car):
    def __init__(self, brand, model, year, rate_per_day):
        super().__init__(brand, model, year, rate_per_day)

    def calculate_rent(self, days):
        return self.rate_per_day * days


class RentalService:
    def __init__(self):
        self.cars = []

    def add_car(self, car):
        self.cars.append(car)

    def get_available_cars(self):
        return [car for car in self.cars if car.available]

    def rent_car(self, full_name):
        for car in self.cars:
            car_full_name = f"{car.brand} {car.model} ({car.year})"
            if car_full_name == full_name and car.available:
                car.available = False
                return car
        return None

# --- Streamlit App Setup ---
st.title("🚗 Car Rental Management System")

# Session Initialization
if 'service' not in st.session_state:
    st.session_state.service = RentalService()

    # Dummy Cars (added only once)
    st.session_state.service.add_car(RentalCar("Toyota", "Corolla", 2020, 5000))
    st.session_state.service.add_car(RentalCar("Honda", "Civic", 2019, 5500))
    st.session_state.service.add_car(RentalCar("Suzuki", "Swift", 2021, 4500))

# Use service from session state
service = st.session_state.service

# Menu
menu = st.sidebar.selectbox("Choose an option", ["View Available Cars", "Rent a Car", "Add a New Car"])

# View Cars
if menu == "View Available Cars":
    st.header("Available Cars")
    available_cars = service.get_available_cars()
    if available_cars:
        for car in available_cars:
            st.write(car.display_info())
    else:
        st.warning("No cars available at the moment!")

# Rent a Car
elif menu == "Rent a Car":
    st.header("Rent a Car")

    available_cars = service.get_available_cars()
    if available_cars:
        car_options = [f"{car.brand} {car.model} ({car.year})" for car in available_cars]
        selected_car_name = st.selectbox("Select a Car to Rent", car_options)

        days = st.number_input("Enter number of rental days", min_value=1)

        if st.button("Rent Now"):
            rented_car = service.rent_car(selected_car_name)
            if rented_car:
                rent = rented_car.calculate_rent(days)
                st.success(f"You have rented {rented_car.display_info()} for {days} days. Total rent: Rs. {rent}")
            else:
                st.error("Sorry! This car is no longer available.")
    else:
        st.warning("No cars available for rent!")

# Add Car
elif menu == "Add a New Car":
    st.header("Add a New Car")
    brand = st.text_input("Enter Car Brand")
    model = st.text_input("Enter Car Model")
    year = st.number_input("Enter Model Year", min_value=1990, max_value=2025)
    rate = st.number_input("Enter Rate Per Day", min_value=1000)

    if st.button("Add Car"):
        if brand and model:
            service.add_car(RentalCar(brand, model, year, rate))
            st.success("Car added successfully!")
        else:
            st.warning("Please fill in all fields.")
