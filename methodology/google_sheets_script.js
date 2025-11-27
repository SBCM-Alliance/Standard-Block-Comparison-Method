/**
 * ==========================================
 * Standard Block Comparison Method for Google Sheets
 * 標準ブロック比較法 カスタム関数スクリプト
 * ==========================================
 * 
 * 【導入方法 / How to Install】
 * 1. Googleスプレッドシートを開く (Open Google Sheets)
 * 2. メニューの「拡張機能」>「Apps Script」をクリック (Extensions > Apps Script)
 * 3. このコードを貼り付けて保存 (Paste this code and save)
 * 4. シート上で関数として使用可能になります (Use as custom functions)
 * 
 * 【使い方 / Usage】
 * =IMPACT_SCORE(値, ターゲット比率)
 * =IMPACT_VERDICT(インパクト値)
 */

/**
 * 定数設定：日本の統計データに基づく
 * Constants: Based on Japanese statistics
 */
const CONSTANTS = {
  POPULATION: 124000000, // 総人口 (Total Population)
  MUNICIPALITIES: 1718   // 基礎自治体数 (Total Municipalities)
};

/**
 * 標準ブロック（B）を算出するカスタム関数
 * Calculates the Standard Block (B)
 * 
 * @param {number} targetRatio ターゲット属性の比率 (0.0 - 1.0) Default: 1.0
 * @return {number} 標準ブロック数 (Standard Block Capacity)
 * @customfunction
 */
function STANDARD_BLOCK(targetRatio = 1.0) {
  if (typeof targetRatio !== 'number') return "Error: Ratio must be a number";
  return (CONSTANTS.POPULATION * targetRatio) / CONSTANTS.MUNICIPALITIES;
}

/**
 * 実効性インパクト（I）を算出するカスタム関数
 * Calculates the Effectiveness Impact (I)
 * 
 * @param {number} value 発表された成果数（人数・円など） (Announced Value)
 * @param {number} targetRatio ターゲット比率 (0.0 - 1.0) Default: 1.0
 * @return {number} インパクト値 (Impact Score)
 * @customfunction
 */
function IMPACT_SCORE(value, targetRatio = 1.0) {
  if (!value) return 0;
  const block = STANDARD_BLOCK(targetRatio);
  return value / block;
}

/**
 * インパクト値から判定コメントを返す関数
 * Returns a verdict based on the Impact Score
 * 
 * @param {number} score インパクト値 (Impact Score)
 * @return {string} 判定コメント (Verdict)
 * @customfunction
 */
function IMPACT_VERDICT(score) {
  if (score === "") return "";
  if (score < 1.0) return "❌ 誤差レベル (Error Level: < 1.0)";
  if (score < 10.0) return "⚠️ 局所的 (Localized: 1.0 - 9.9)";
  return "✅ 実効性あり (Effective: >= 10)";
}
