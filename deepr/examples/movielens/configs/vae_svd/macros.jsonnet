local macros = import '../common/macros.jsonnet';

macros + {
    run+: {
        run_on_yarn: false
    },
    mlflow+: {
        use_mlflow: false
    },
    params+: {
        target_ratio: null,
        normalize_embeddings: true,
        share_embeddings: true,
        num_negatives: null,
        loss: "multi",
        train_embeddings: false,
        project: false,
    }
}
