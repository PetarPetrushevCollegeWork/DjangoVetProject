const kcalPerGram = 3.6;
const activityMultiplyer = { low: 0.9, normal: 1.0, high: 1.2 };

function lifeStageFactor(ageYears) {
  if (ageYears < 1) return 2.5;
  if (ageYears < 8) return 1.6;
  return 1.2;
}

function dailyNeeds(weightKg, ageYears, activity) {
  const restingEnergyNeed = 70 * Math.pow(weightKg, 0.75);
  const kcalNeed =
    restingEnergyNeed *
    lifeStageFactor(ageYears) *
    activityMultiplyer[activity];

  return {
    kcal: Math.round(kcalNeed),
    grams: Math.round(kcalNeed / kcalPerGram),
  };
}

function calculatePetFood(document) {
  const weightInput = document.getElementById("weightInput");
  const ageInput = document.getElementById("ageInput");
  const activityInput = document.getElementById("activityInput");
  const resultDiv = document.getElementById("result");

  const result = dailyNeeds(
    weightInput.value,
    ageInput.value,
    activityInput.value,
  );
  const resultText =
    "Your pet needs <b>" + result.grams + "g</b> of food per day.";
  resultDiv.innerHTML = resultText;
}
