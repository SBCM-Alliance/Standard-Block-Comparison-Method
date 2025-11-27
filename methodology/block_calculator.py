import argparse
import sys

# 定数定義 (日本の統計データに基づく)
# 2023年推計人口など適宜更新可能
DEFAULT_POPULATION = 124_000_000  # 日本の総人口
DEFAULT_MUNICIPALITIES = 1_718    # 基礎自治体数

def calculate_standard_block(population, target_ratio, municipalities):
    """
    標準ブロック（1自治体あたりの平均ターゲット数）を算出する
    """
    return (population * target_ratio) / municipalities

def calculate_impact(value, standard_block):
    """
    実効性インパクト（I）を算出する
    """
    if standard_block == 0:
        return 0
    return value / standard_block

def get_verdict(impact):
    """
    インパクト値に基づいて、詳細な「社会実装ステージ」を判定する
    基準：
    - I < 1.0: 誤差
    - I < 14.0: 局所的 (郵便局未満)
    - I < 32.0: 基礎インフラ (郵便局超え、コンビニ未満)
    - I < 700.0: コンビニ級 (コンビニ超え、人口1%未満)
    - I < 7000.0: 普及フェーズ (人口1%超え)
    - I >= 7000.0: 社会OS (人口10%超え)
    """
    if impact < 1.0:
        return "💀【誤差レベル (Error)】\n   判定: 1自治体すらカバーできていません。社会インフラとして機能不全です。"
    
    elif impact < 14.0:
        return "⚠️【局所的 (Localized)】\n   判定: 一部地域での実験段階です。郵便局(I=14)のような「基礎インフラ」には達していません。"
    
    elif impact < 32.0:
        return "🏠【基礎インフラ級 (Infrastructure)】\n   判定: 郵便局(I=14)と同等の密度です。物理的な拠点としては十分ですが、デジタルとしては物足りません。"
    
    elif impact < 700.0:
        return "🏪【コンビニ級 (Convenience)】\n   判定: コンビニ(I=32)を超えています。生活圏に浸透していますが、住民全体の認知(1%)には届いていません。"
    
    elif impact < 7000.0:
        return "🚀【普及フェーズ (Penetration)】\n   判定: 人口の1%を超えました。アーリーアダプターに届き、自律的な普及が始まっています。"
    
    else:
        return "👑【社会OS級 (Social OS)】\n   判定: 人口の10%を超えました。水道や電気のように、なくてはならない社会基盤です。"

def main():
    parser = argparse.ArgumentParser(
        description='標準ブロック比較法 (Standard Block Comparison Method) 計算ツール v2.0'
    )
    
    # 必須引数
    parser.add_argument(
        '--value', '-v',
        type=float,
        required=True,
        help='発表された成果数（例: 利用者数3000人なら 3000、予算1億円なら 100000000）'
    )

    # オプション引数
    parser.add_argument(
        '--target_ratio', '-r',
        type=float,
        default=1.0,
        help='ターゲット属性の比率 (0.0 〜 1.0)。デフォルトは1.0（全人口）'
    )
    
    parser.add_argument(
        '--population', '-p',
        type=int,
        default=DEFAULT_POPULATION,
        help=f'総人口。デフォルトは {DEFAULT_POPULATION:,}'
    )
    
    parser.add_argument(
        '--municipalities', '-m',
        type=int,
        default=DEFAULT_MUNICIPALITIES,
        help=f'基礎自治体数。デフォルトは {DEFAULT_MUNICIPALITIES:,}'
    )

    args = parser.parse_args()

    # 計算実行
    try:
        standard_block = calculate_standard_block(
            args.population, 
            args.target_ratio, 
            args.municipalities
        )
        
        impact = calculate_impact(args.value, standard_block)
        
        # 結果表示
        print("\n=== 標準ブロック比較法 分析結果 (v2.0) ===")
        print(f"1. 入力値 (Value):       {args.value:,.0f}")
        print(f"2. ターゲット比率:       {args.target_ratio * 100:.1f}%")
        print("-" * 40)
        print(f"3. 標準ブロック (B):     {standard_block:,.1f} (1自治体あたりのキャパシティ)")
        print(f"4. 実効性インパクト (I): {impact:.4f}")
        print("-" * 40)
        print(f"結論: {get_verdict(impact)}")
        print("========================================\n")

    except Exception as e:
        print(f"エラーが発生しました: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
