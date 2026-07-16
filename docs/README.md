price = float(input("Enter the price of one item: "))
quantity = int(input("Enter the quantity: "))

total = price * quantity

print(f"{quantity} items at {price:.2f} each = {total:.2f}")
# Python Lab - Documentation

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Budget Tracker</title>
  <link rel="stylesheet" href="style.css" />
</head>
<body>
  <header class="page-header">
    <!-- Part 3: Multimedia — logo image with src / alt / width -->
    <img
      class="logo"
      src="assets/logo.png"
      alt="Budget Tracker logo"
      width="64"
    />
    <h1>Budget Tracker</h1>
  </header>

  <main>
    <!-- Part 3: Multimedia — embedded YouTube video -->
    <section class="video-section">
      <h2>Getting Started</h2>
      <iframe
        width="560"
        height="315"
        src="https://www.youtube.com/embed/dQw4w9WgXcQ"
        title="How to budget: a beginner's guide"
        frameborder="0"
        allowfullscreen
      ></iframe>
    </section>

    <!-- Part 4: Interactive — collapsible details/summary -->
    <details class="tips" open>
      <summary>Budgeting tips (click to expand)</summary>
      <p>
        Track every expense as it happens, group spending into categories, and
        review your totals weekly to catch overspending early.
      </p>
    </details>

    <!-- Part 1: Expense table -->
    <section class="expenses">
      <h2>Expenses</h2>
      <table class="expense-table">
        <thead>
          <tr>
            <th>Name</th>
            <th>Amount</th>
            <th>Category</th>
            <th>Date</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>Groceries</td>
            <td>$82.40</td>
            <td>Food</td>
            <td>2026-07-01</td>
          </tr>
          <tr>
            <td>Bus Pass</td>
            <td>$45.00</td>
            <td>Transport</td>
            <td>2026-07-03</td>
          </tr>
          <tr>
            <td>Apartment</td>
            <td>$1,200.00</td>
            <td>Rent</td>
            <td>2026-07-05</td>
          </tr>
          <tr>
            <td>Movie Night</td>
            <td>$28.50</td>
            <td>Entertainment</td>
            <td>2026-07-08</td>
          </tr>
          <tr>
            <td>Phone Bill</td>
            <td>$60.00</td>
            <td>Other</td>
            <td>2026-07-10</td>
          </tr>
          <tr>
            <td>Coffee</td>
            <td>$12.75</td>
            <td>Food</td>
            <td>2026-07-12</td>
          </tr>
        </tbody>
      </table>
    </section>

    <!-- Part 2: Upgraded Add Expense form -->
    <section class="add-expense">
      <h2>Add Expense</h2>
      <form id="expense-form">
        <div class="field">
          <label for="expense-name">Name</label>
          <input type="text" id="expense-name" name="expense-name" placeholder="e.g. Groceries" />
        </div>

        <div class="field">
          <label for="expense-amount">Amount</label>
          <input type="number" id="expense-amount" name="expense-amount" step="0.01" min="0" placeholder="0.00" />
        </div>

        <div class="field">
          <label for="expense-category">Category</label>
          <select id="expense-category" name="expense-category">
            <option value="food">Food</option>
            <option value="transport">Transport</option>
            <option value="rent">Rent</option>
            <option value="entertainment">Entertainment</option>
            <option value="other">Other</option>
          </select>
        </div>

        <div class="field">
          <label for="expense-date">Date</label>
          <input type="date" id="expense-date" name="expense-date" />
        </div>

        <button type="button" id="add-expense-btn">Add Expense</button>
      </form>
    </section>
  </main>

  <footer class="page-footer">
    <p>&copy; 2026 Budget Tracker. Built for Week 2.</p>
  </footer>
</body>
</html>
/* ===== Base ===== */
body {
  font-family: system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;
  margin: 0;
  padding: 0;
  color: #1f2933;
  background: #f5f7fa;
  line-height: 1.5;
}

main {
  max-width: 760px;
  margin: 0 auto;
  padding: 1.5rem;
}

/* ===== Header (multimedia: logo) ===== */
.page-header {
  display: flex;
  align-items: center;
  gap: 1rem;
  padding: 1rem 1.5rem;
  background: #1e3a8a;
  color: #ffffff;
}

.logo {
  border-radius: 8px;
}

h1,
h2 {
  margin: 0.5rem 0;
}

/* ===== Video ===== */
.video-section iframe {
  max-width: 100%;
  border-radius: 8px;
}

/* ===== Part 1: Expense table ===== */
.expense-table {
  width: 100%;
  border-collapse: collapse;      /* required */
  background: #ffffff;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
}

.expense-table th,
.expense-table td {
  padding: 0.75rem 1rem;          /* required padding */
  text-align: left;
  border-bottom: 1px solid #e4e7eb;
}

/* colored header (required) */
.expense-table thead th {
  background: #2563eb;
  color: #ffffff;
}

/* zebra striping (required) */
.expense-table tbody tr:nth-child(even) {
  background: #eef2ff;
}

/* Part 4: row hover interaction */
.expense-table tbody tr:hover {
  background: #dbeafe;
}

/* ===== Part 2: Form ===== */
.field {
  margin-bottom: 1rem;
  display: flex;
  flex-direction: column;
  max-width: 320px;
}

.field label {
  font-weight: 600;
  margin-bottom: 0.25rem;
}

.field input,
.field select {
  padding: 0.5rem;
  border: 1px solid #cbd2d9;
  border-radius: 6px;
  font-size: 1rem;
}

/* Advanced selector: :focus */
.field input:focus,
.field select:focus {
  outline: none;
  border-color: #2563eb;
  box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.25);
}

/* Part 4: button cursor pointer */
#add-expense-btn {
  cursor: pointer;
  background: #2563eb;
  color: #ffffff;
  border: none;
  padding: 0.6rem 1.2rem;
  border-radius: 6px;
  font-size: 1rem;
}

#add-expense-btn:hover {
  background: #1d4ed8;
}

/* ===== Part 5: Advanced selectors ===== */

/* 1. Descendant selector */
.add-expense label {
  color: #334e68;
}

/* 2. Direct-child selector */
.tips > summary {
  font-weight: 700;
  cursor: pointer;
}

/* 3. Positional pseudo-class (first cell of each row) */
.expense-table td:first-child {
  font-weight: 600;
}

/* 4. :not() — style every field except the last one differently */
.field:not(:last-of-type) {
  border-left: 3px solid transparent;
}

/* ===== Details / footer ===== */
.tips {
  background: #ffffff;
  padding: 1rem;
  border-radius: 8px;
  margin: 1rem 0;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
}

.page-footer {
  text-align: center;
  padding: 1rem;
  color: #627d98;
  font-size: 0.9rem;
}
