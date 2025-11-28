import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sbcm import config, block_calculator, budget_distortion_analyzer

# ページ設定
st.set_page_config(
    page_title="Standard Block Auditor",
    page_icon="⚖️",
    layout="wide"
)

# タイトル
st.title("⚖️ Standard Block Comparison Method (SBCM)")
st.markdown("""
**行政の「数字のマジック」を暴くための定量的監査ツール**  
予算や成果数値を「基礎自治体（Standard Block）」単位に正規化し、その実効性を判定します。
""")

# タブで機能を分ける
tab1, tab2, tab3 = st.tabs(["🧮 単発インパクト計算", "📂 決算書ファイル分析", "📖 理論解説"])

# --- タブ1: 単発計算 ---
with tab1:
    st.header("単発の成果・予算を検証する")
    col1, col2 = st.columns(2)
    
    with col1:
        input_val = st.number_input("発表された数値 (人/円)", min_value=0.0, value=3000.0, step=100.0)
        input_ratio = st.slider("ターゲット比率 (全人口=1.0)", 0.0, 1.0, 1.0, 0.01)
    
    if st.button("計算実行 (Calculate)", type="primary"):
        # 計算ロジック
        std_block = block_calculator.calculate_standard_block(
            config.NATIONAL_POPULATION, input_ratio, config.TOTAL_MUNICIPALITIES
        )
        impact = block_calculator.calculate_impact(input_val, std_block)
        verdict = block_calculator.get_verdict(impact)
        
        # 結果表示
        st.divider()
        c1, c2, c3 = st.columns(3)
        c1.metric("標準ブロック人口", f"{std_block:,.0f} 人")
        c2.metric("実効性インパクト (I)", f"{impact:.4f}")
        
        st.subheader("判定結果")
        if impact < 1.0:
            st.error(verdict)
        elif impact < 17.2:
            st.warning(verdict)
        elif impact < 172.0:
            st.info(verdict)
        else:
            st.success(verdict)

# --- タブ2: CSV分析 ---
with tab2:
    st.header("決算書CSVの歪み分析")
    st.markdown("`事業名`, `決算額`, `推定受益者数` の3列を持つCSVをアップロードしてください。")
    
    uploaded_file = st.file_uploader("CSVファイルをアップロード", type="csv")
    city_pop = st.number_input("自治体の人口 (例: 柏市=435000)", value=435000)

    if uploaded_file is not None:
        try:
            df = pd.read_csv(uploaded_file)
            
            # 分析実行 (既存ロジックの再利用)
            # config経由で定数を利用
            scale_factor = city_pop / config.STD_BLOCK_POP
            local_std_budget = config.STD_BUDGET_UNIT * scale_factor
            
            results = []
            for index, row in df.iterrows():
                budget = row['決算額']
                users = row['推定受益者数']
                i_budget = budget / local_std_budget
                i_coverage = users / config.STD_BLOCK_POP
                
                if i_coverage <= 0.0001:
                    d_index = 9999.0
                else:
                    d_index = i_budget / i_coverage

                verdict = "✅ 適正"
                if d_index > 50: verdict = "🚨 異常な歪み"
                elif d_index > 10: verdict = "⚠️ 高コスト"
                elif d_index < 1: verdict = "💎 高効率"

                results.append({
                    '事業名': row['事業名'],
                    '決算額': budget,
                    '普及Imp': i_coverage,
                    '予算Imp': i_budget,
                    '歪み指数': d_index,
                    '判定': verdict
                })
            
            res_df = pd.DataFrame(results).sort_values('歪み指数', ascending=False)
            
            # 結果テーブル表示
            st.dataframe(res_df.style.format({'決算額': '{:,.0f}', '歪み指数': '{:.1f}', '普及Imp': '{:.4f}'}))
            
            # グラフ描画
            st.subheader("予算ポートフォリオ分析 (Budget Distortion Matrix)")
            fig, ax = plt.subplots(figsize=(10, 6))
            
            # 日本語フォント対策 (Streamlit Cloudでは英語が無難だが、とりあえず描画)
            scatter = ax.scatter(
                res_df['普及Imp'], 
                res_df['予算Imp'], 
                s=res_df['歪み指数']*20, 
                c=res_df['歪み指数'], 
                cmap='coolwarm', 
                alpha=0.7, 
                edgecolors="grey"
            )
            ax.set_xscale('log')
            ax.set_yscale('log')
            ax.axvline(x=1.0, color='gray', linestyle='--')
            ax.axhline(y=1.0, color='gray', linestyle='--')
            ax.set_xlabel('Impact (Coverage)')
            ax.set_ylabel('Impact (Budget)')
            plt.colorbar(scatter, label='Distortion Index')
            
            st.pyplot(fig)

        except Exception as e:
            st.error(f"エラーが発生しました: {e}")

# --- タブ3: 理論 ---
with tab3:
    st.markdown(open("README.md", encoding='utf-8').read())
