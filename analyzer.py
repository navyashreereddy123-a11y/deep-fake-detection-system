def analyze_results(t_score, s_score):
    confidence = (t_score + s_score) / 2

    if t_score > s_score:
        reason = "Temporal inconsistency detected"
    else:
        reason = "Abnormal signal pattern detected"

    if confidence > 50:
        label = "FAKE"
    else:
        label = "REAL"

    return {
        "label": label,
        "confidence": round(confidence, 2),
        "reason": reason
    }